from datetime import datetime, timedelta
from jose import jwt , JWTError
from passlib.context import CryptContext
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from src.db import login_collection, gamestates_collection
from src.models import UserRegister
import bcrypt
import datetime
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")


SECRET_KEY = "EFHEIORFHUEZIHSZOCHJZOEIHF"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 360

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password : str, hashed_password: str):
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def get_password_hash(password: str):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])        
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    user = login_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(user_data: UserRegister):
    existing_user = login_collection.find_one({"username": user_data.username})
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Ce nom d'utilisateur est déjà pris."
        )
    hashed_password = get_password_hash(user_data.password)

    new_user = {
        "username": user_data.username,
        "hashed_password": hashed_password,
    }
    login_collection.insert_one(new_user)
    gamestates_collection.insert_one({
        "name": user_data.username,
        "current_chatroom_id": 1,
        "current_message_id": 0,
        "id_of_last_choice": 0,
        "history": [],
        "points": []
    })

    return {"message": "Utilisateur créé avec succès !"}