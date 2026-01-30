from fastapi import APIRouter , HTTPException, status
from typing import List
from src.db import messages_collection , gamestates_collection
from src.models import Message
from pymongo import ReturnDocument

router = APIRouter()


@router.get("/send/{player_name}", response_model=Message) #Envoi du prochain message a afficher qui est dans la bonne branche
def send_next_message(player_name: str):
    current_chatroom_id = gamestates_collection.find_one({"name": player_name})["current_chatroom_id"]
    current_message_id = gamestates_collection.find_one({"name": player_name})["current_message_id"]
    chatroom_messages = get_chatroom_messages(current_chatroom_id)
    player_history = get_player_history(player_name)
    current_branch = player_history[-1]["choices"][-1]["choice"] if player_history else 0 #peut etre directement écrire la branche en cours quelque part en sauvegarde
    count=0
    for message in chatroom_messages:
        if count != current_message_id:
            count+=1
        else:
            increment_current_message_id(player_name)
            if message["branch"] != current_branch and message["branch"] != 0:
                count+=1
                current_message_id += 1
            else: 
                if message["character"] != "Player":
                    return Message(character=message["character"], content=message["content"], channel=message["channel"])
                else:
                    return Message(character=message["character"], choices=message["choices"], channel=message["channel"])

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No more messages in this chatroom")

def increment_current_message_id(player_name: str):
    updated = gamestates_collection.find_one_and_update(
            {"name": player_name},
            {"$inc": {"current_message_id": 1}},
            return_document=ReturnDocument.AFTER
    )

@router.get("/recv/{player_name}/{channel_name}/{answer}")
def receive_player_answer(player_name: str, channel_name:str, answer :int):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    new_choice = {"channel": channel_name, "choice": int(answer)}
    history = player.get("history", [])
    if not isinstance(history, list):
        history = []
    if not history:
        new_entry = {
            "chatroom_id": player.get("current_chatroom_id"),
            "choices": [new_choice]
        }
        gamestates_collection.update_one({"name": player_name}, {"$push": {"history": new_entry}})




@router.get("/history/full/{player_name}/{channel_name}", response_model=List[Message])
def get_full_history(player_name :str, channel_name :str) -> List[Message]: #get de tout les messages d'une conversation donnée jusqu'au dernier choix.
    player_history = get_player_history(player_name)
    messages_history: List[Message] = []
    for history in player_history:
        messages = get_chatroom_messages(history["chatroom_id"])
        choices_history=get_choices_history(channel_name, history["choices"])
        messages_history.extend(get_messages(messages, channel_name, choices_history))
    messages_history.extend(get_last_messages(player_name,channel_name))
    return messages_history



@router.get("/history/end/{player_name}")
def end_chatroom(player_name: str):
    current_chatroom_id = gamestates_collection.find_one({"name": player_name})["current_chatroom_id"]
    gamestates_collection.update_one(
        {"name": player_name},
        {
            "$set": {
                "current_chatroom_id": current_chatroom_id + 1,
                "current_message_id": 0,
                "id_of_last_choice": 0
            }
        }
    )
    return {"message": f"Player {player_name} has ended chatroom {current_chatroom_id}."}

def get_last_messages(player_name: str, channel_name) -> List[Message]: # Renvoie les messages après le dernier choix jusqu'au message actuel dans la sauvegarde
    current_chatroom_id = gamestates_collection.find_one({"name": player_name})["current_chatroom_id"]
    current_message_id = gamestates_collection.find_one({"name": player_name})["current_message_id"]
    id_of_last_choice = gamestates_collection.find_one({"name": player_name})["id_of_last_choice"]
    chatroom_messages = get_chatroom_messages(current_chatroom_id)
    messages_after_choice: List[Message] = []
    count=0
    for message in chatroom_messages:
        if message["channel"] == channel_name and count> id_of_last_choice and count <= current_message_id:
            messages_after_choice.append(Message(character=message["character"], content=message["content"]))
        count+=1
    return messages_after_choice

def get_chatroom_messages(chatroom_id): # Renvoie tous les messages d'une chatroom
    return list(messages_collection.find({"id":chatroom_id})[0]["messages"])


def get_choices_history(channel_name: str, choices: List[dict]) -> List[int]: #get l'historique des choix pour une conversation (enleve les choices qui ne sont pas liées a la conversation donnée)
    choices_history = []
    for choice in choices:
        if choice["channel"] == channel_name:
            choices_history.append(choice["choice"])
    return choices_history

def get_messages(messages: List[Message], channel_name: str, choices_history: List[int]) -> List[Message]: #get des messages a selectionner dans une conversation.
    current_branch = 0
    messages_history: List[Message] = []
    for message in messages:
        print(choices_history)
        if message["channel"] == channel_name and choices_history !=[]:   
            if (message["branch"] == current_branch or message["branch"] == 0) and message["character"] != "Player":
                messages_history.append(Message(character=message["character"], content=message["content"]))
            elif message["character"] == "Player":
                current_branch = choices_history.pop(0)
                content=message["choices"]
                choice=content[current_branch -1]["text"]
                messages_history.append(Message(character=message["character"], content=choice))    
    return messages_history


def get_player_history(player_name: str) -> List[dict]: # Renvoie l'historique complet d'un joueur
    player_gamestate = gamestates_collection.find_one({"name": player_name})
    if not player_gamestate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    history = player_gamestate.get("history", [])
    if not isinstance(history, list):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid history format")
    return history



def is_text(content: str) -> bool: 
    return content.startswith("src/assets/")
