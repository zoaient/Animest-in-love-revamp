from fastapi import APIRouter , HTTPException, status
from typing import List
from src.db import messages_collection , gamestates_collection
from src.models import Message
from pymongo import ReturnDocument

router = APIRouter()


@router.get("/send/{player_name}", response_model=Message) #Envoi du prochain message a afficher  
def send_next_message(player_name: str):
    current_chatroom_id = gamestates_collection.find_one({"name": player_name})["current_chatroom_id"]
    current_message_id = gamestates_collection.find_one({"name": player_name})["current_message_id"]
    chatroom_messages = get_chatroom_messages(current_chatroom_id)
    count=0
    for message in chatroom_messages:
        if count != current_message_id:
            count+=1
        else:
            increment_current_message_id(player_name)
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
    return 

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























@router.get("/next_messages/{player_name}/{branch_choice}", response_model=List[Message]) #Ici, tout envoyer en fonction de la branche selectionnée, la fonction va de choix en choix , get le gamestate aussi , s'occupe aussi de maj l'historique
def get_next_messages(player_name, branch_choice):
    player_gamestate = list(gamestates_collection.find({"name": player_name}))
    current_chatroom_id = player_gamestate[0]["current_chatroom_id"] 
    current_message_id = player_gamestate[0]["current_message_id"] -1
    chatroom_text = list(messages_collection.find({"id" : int(current_chatroom_id)-1}))
    all_messages=chatroom_text[0]["messages"]  
    Player_found = False
    displayed_messages = []
    while current_message_id<len(all_messages) and not Player_found :
        if all_messages[current_message_id]["character"]=="Player":
            Player_found = True
        if all_messages[current_message_id]["branch"]==int(branch_choice) or not all_messages[current_message_id]["branch"]:     
            displayed_messages.append(all_messages[current_message_id])
        current_message_id+=1
    current_message_id+=1

    return displayed_messages


@router.get("/history/{player_name}/{channel_name}", response_model=List[Message])
def get_history(channel_name,player_name):
    player_gamestate = list(gamestates_collection.find({"name": player_name}))
    player_history =player_gamestate[0]["history"]
    messages_history=[]

    for history in player_history:
        messages =get_chatroom_messages(history["chatroom_id"])
        past_choices =history["choices"]
        current_branch = past_choices[0]
        branch_counter = 0
        has_branch_started =False
        for message in messages:
            if message["channel"] ==channel_name:
                if  message["branch"]==current_branch or not message["branch"]:
                    if message["character"]!="Player":
                        messages_history.append(message)
                    else:
                        player_choices = message["choices"]
                        player_message={'id': 0, 'character': 'Player', 'picture_or_text': 'text', 'content': '', 'channel': channel_name, 'branch': 0}
                        for choice in player_choices:
                            if choice['id']==current_branch:
                                player_message['content']=choice['text']
                        messages_history.append(player_message)
                    has_branch_started=True
                elif has_branch_started:
                    has_branch_started=False
                    if(branch_counter+1<len(past_choices)):
                        branch_counter+=1
                        current_branch=past_choices[branch_counter]
    return messages_history
