from fastapi import APIRouter
from typing import List
from src.db import characters_collection
from src.models import Character

router = APIRouter()

@router.get("/characters", response_model=List[Character])
def get_all_characters():
    characters = list(characters_collection.find({}))
    print(characters)
    return characters

