from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:5173", 
    "http://localhost:5174", 
    "http://localhost:8080", 
]
from db import characters_collection
from models import Character
from typing import List

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)


@app.get("/api/characters", response_model=List[Character])
def get_all_characters(): 
    characters = list(characters_collection.find({}))
    return characters

@app.get("/")
async def root():
    return {"message": "Le serveur FastAPI fonctionne !"}