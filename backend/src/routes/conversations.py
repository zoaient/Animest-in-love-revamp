from fastapi import APIRouter
from typing import List
from src.db import messages_collection
from src.models import Message

router = APIRouter()

@router.get("/conversation", response_model=List[Message])
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