from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app= FastAPI()

@app.get("/messo")

async def one():
    return {"message":"hello world"}


@app.post("/")

async def post():
    return {"message":"hello world"}


@app.put("/")

async def put():
    return {"message":"hello world"}


@app.get("/item/me")
async def current():
    return {"message":"I am the current user"}

@app.get("/item/{itemId}")
async def get_item(itemId:int):
    return {"item":itemId}




class foodEnum (str , Enum):
    fruits="fruits"
    vegetables="vegetables"
    drinks="drinks"

@app.get("/food/{foodName}")
async def get_food(foodName:foodEnum):
    if foodName==foodEnum.fruits:
        return {"foodName":foodName,"mesaage":"you like sweet food"}
    elif foodName.value=="drinks":
        return {"foodName":foodName,"mesaage":"you are thirsty"}
    else:
        return{"foodName":foodName,"mesaage":"you are not healthy"}





fakenames=[{"firstName":"Jos"},{"firstName":"Joe"},{"firstName":"Mary"}]

@app.get("/items")
async def getItems(skip:int=0, limit:int=10):
    return fakenames[skip: skip+limit]
#http://127.0.0.1:8000/items?skip=2
    #returns [{"firstName":"Mary"}]

#http://127.0.0.1:8000/items?skip=0
    #returns [{"firstName":"Jos"},{"firstName":"Joe"},{"firstName":"Mary"}]


@app.get("/items/{itemId}")
async def list(itemId:str,q:Optional[str]=None):
    if q:
        return {"itemid":itemId,"q":q}
    return {"itemid":itemId}




#REQUEST BODY
class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:float |  None=None   

app.post('./items')
async def createItem():
    return item
