from fastapi import APIRouter , HTTPException, status , Depends
from src.db import gamestates_collection
from src.routes.login import get_current_user

router = APIRouter()

 
@router.get("/create") # A priori inutile maintenant qu'il y'a register
def create_player_gamestate(player_name: str):
    existing_player = gamestates_collection.find_one({"name": player_name})
    if existing_player:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player gamestate already exists")
    
    new_gamestate = {
        "name": player_name,
        "profile_picture": "none",
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



@router.get("/reset")
def reset_player_gamestate(player_name: str = Depends(get_current_user)):
    gamestates_collection.update_one(
        {"name": player_name},
        {
            "$set": {
                "profile_picture" : "src/assets/Pfp/katharine_pdp.png",
                "current_chatroom_id": 1,
                "current_message_id": 0,
                "id_of_last_choice": 0,
                "history": []
            }
        }
    )
    return {"message": f"Player {player_name} gamestate has been reset."}

@router.get("/delete")
def delete_player_gamestate(player_name: str = Depends(get_current_user)):
    result = gamestates_collection.delete_one({"name": player_name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    return {"message": f"Player {player_name} gamestate has been deleted."}


@router.get("/points")
def get_player_points(player_name: str = Depends(get_current_user)):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    points = player.get("points", 0)
    return {"player_name": player_name, "points": points}

@router.get("/message_id")
def get_player_message_id(player_name: str = Depends(get_current_user)):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    message_id = player.get("current_message_id", 0)
    return {"player_name": player_name, "message_id": message_id}

@router.get("/choices")
def get_player_choices(player_name: str = Depends(get_current_user)):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    history = player.get("history", [])
    if not isinstance(history, list):
        history = []
    return {"player_name": player_name, "choices_history": history}

@router.get("/chatroom_id")
def get_player_chatroom_id(player_name: str = Depends(get_current_user)) :
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    chatroom_id = player.get("current_chatroom_id", 0)
    return {"player_name": player_name, "chatroom_id": chatroom_id} 

@router.get("/set_profile_picture")
def set_profile_picture(profile_picture: str,player_name: str = Depends(get_current_user)):
    gamestates_collection.update_one(
        {"name": player_name},
        {
            "$set": {
                "profile_picture" : profile_picture
            }
        }
    )
    return {"message": f"Player {player_name} profile picture has"}

@router.get("/profile_picture")
def get_profile_picture(player_name: str = Depends(get_current_user)):
    player = gamestates_collection.find_one({"name": player_name})
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player gamestate not found")
    profile_picture = player.get("profile_picture", 0)
    return {profile_picture} 