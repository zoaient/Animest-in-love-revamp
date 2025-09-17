from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:5173", 
    "http://localhost:5174", 
    "http://localhost:8080", 
]
from src.routes import characters , conversations

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)


app.include_router(
    characters.router,
    prefix="/api",   
    tags=["Characters"]   
)

app.include_router(
    conversations.router,
    prefix="/api",   
    tags=["Conversations"]   
)

@app.get("/")
async def root():
    return {"message": "Le serveur FastAPI fonctionne !"}

