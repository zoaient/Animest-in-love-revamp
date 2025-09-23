from fastapi import APIRouter
from typing import List
from src.db import messages_collection , gamestates_collection
from src.models import Message

router = APIRouter()

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

def get_chatroom_messages(chatroom_id):
    return list(messages_collection.find({"id":chatroom_id})[0]["messages"])

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


