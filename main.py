from enum import Enum

from fastapi import FastAPI

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


