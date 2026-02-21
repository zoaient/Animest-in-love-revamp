from fastapi import APIRouter
from src.db import messages_collection

router = APIRouter()
#../../chatrooms/sample.txt
@router.get("/parse")
async def parse_conversation(filename : str):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    lines=remove_empty_lines(lines)
    chatroom_name=lines[0].split(":")[-1].lstrip() 
    characters=lines[1].split(":")[-1].split(",") #TODO : Pdp sur la convo ? 
    room_id=int(lines[2].split(":")[-1].lstrip())
    branch = 0
    channel = ""
    id=1
    messages=[]
    del lines[0:3]
    for line in lines:
        line_split = line.split(":")
        index = line_split[0].rsplit()[0]
        content = line_split[1]
        if index=="Branch":
            branch=int(content.rsplit()[0])
        elif index=="Channel":
            channel=content.rsplit()[0]
        elif index=="Player":
            content=content.split(";")
            choices=[]
            for i in range(0,len(content),2):
                text=content[i][1:-1]
                points=content[i+1] #TODO : systeme de points
                answer={"id": i//2+1, "text":text}
                choices.append(answer)

            entry={"id":id,
                   "character":"Player",
                   "choices":choices,
                   "channel":channel,
                   "branch":branch,
                   }
            id+=1
            messages.append(entry)
        else:
            entry={"id":id,
                   "character":index,
                   "content":content[1:],
                   "channel":channel,
                   "branch":branch,
                  }
            id+=1
            messages.append(entry)      
    chatroom={"id":room_id,
            "characters":characters,
            "chatroom_name":chatroom_name,
            "messages":messages,
            }
    
    messages_collection.insert_one(chatroom)
    return {"message": f"Chatroom {chatroom_name} has been created."}

def remove_empty_lines(all_lines: list[str]):
    lines=[]
    for line in all_lines:
        if not line=="":
            lines.append(line)
    return lines