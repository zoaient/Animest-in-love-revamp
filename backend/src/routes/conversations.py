from fastapi import APIRouter
from typing import List
from src.db import messages_collection , gamestates_collection
from src.models import Message

router = APIRouter()

@router.get("/next_messages", response_model=List[Message]) #Ici, tout envoyer en fonction de la branche selectionnée, la fonction va de choix en choix , get le gamestate aussi
def get_next_messages():
    chatroom_text = list(messages_collection.find({}))
    all_messages=chatroom_text[0]["messages"]  
    game_state =3
    Player_found = False
    displayed_messages = []
    while game_state<len(all_messages) and not Player_found:
        if all_messages[game_state]["character"]=="Player":
            Player_found = True
        else:
            all_messages
        displayed_messages.append(all_messages[game_state])
        game_state+=1
        
    print(displayed_messages)
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
        choices =history["choices"]
        current_branch = choices[0]
        branch_counter = 0
        has_branch_started =False
        for message in messages:
            if message["channel"] ==channel_name:
                if  message["branch"]==current_branch or not message["branch"]:
                    messages_history.append(message)
                    has_branch_started=True
                elif has_branch_started:
                    has_branch_started=False
                    if(branch_counter+1<len(choices)):
                        branch_counter+=1
                        current_branch=choices[branch_counter]
    return messages_history


