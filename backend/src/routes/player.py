from fastapi import APIRouter , HTTPException, status
from typing import List
from src.db import gamestates_collection
from src.models import Message
from pymongo import ReturnDocument

router = APIRouter()

@router.get("/reset/{player_name}")
def reset_player_gamestate(player_name: str):
    gamestates_collection.update_one(
        {"name": player_name},
        {
            "$set": {
                "current_chatroom_id": 1,
                "current_message_id": 0,
                "id_of_last_choice": 0,
                "history": []
            }
        }
    )
    return {"message": f"Player {player_name} gamestate has been reset."}

@router.get("/create/{player_name}")
def create_player_gamestate(player_name: str):
    existing_player = gamestates_collection.find_one({"name": player_name})
    if existing_player:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player gamestate already exists")
    
    new_gamestate = {
        "name": player_name,
        "current_chatroom_id": 1,
        "current_message_id": 0,
        "id_of_last_choice": 0,
        "history": [],
        "points": [
            {"name" : "Arthur" , "points" : 0},
            {"name" : "b" , "points" : 0},
        ]
    }
    gamestates_collection.insert_one(new_gamestate)
    return {"message": f"Player {player_name} gamestate has been created."}

@router.get("/delete/{player_name}")
def delete_player_gamestate(player_name: str):
    result = gamestates_collection.delete_one({"name": player_name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    return {"message": f"Player {player_name} gamestate has been deleted."}

@router.get("/points/{player_name}")
def get_player_points(player_name: str):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    points = player.get("points", 0)
    return {"player_name": player_name, "points": points}

@router.get("/message_id/{player_name}")
def get_player_message_id(player_name: str):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    message_id = player.get("current_message_id", 0)
    return {"player_name": player_name, "message_id": message_id}

@router.get("/choices/{player_name}")
def get_player_choices(player_name: str):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    history = player.get("history", [])
    if not isinstance(history, list):
        history = []
    return {"player_name": player_name, "choices_history": history}