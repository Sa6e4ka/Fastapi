from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse 
from fastapi.exceptions import ValidationException

from pydantic import BaseModel, Field, PositiveInt

from fastapi_users import FastAPIUsers




app = FastAPI(
    title="Goofy ah app",
)


@app.exception_handler(ValidationException)
async def validate(request : Request, exc : ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "detail" : exc.errors()
            }
        )
    )


userslist = [
    {"id" : 1, "name" : "bob", "achievements" : [
        {
            "name" : "the biggest cock in the world",
            "date" : "2023-04-07"
        }
    ]},
    {"id" : 2, "name" : "mob"},
    {"id" : 3, "name" : "cob"},
    {"id" : 4, "name" : "lob"},
    {"id" : 5, "name" : "pob"},

]

class Achievement(BaseModel):
    ach_name : str
    date : str
    

class Users(BaseModel):
    id : PositiveInt
    name : str = Field(max_length=15)
    achievement : Achievement = None 

@app.get("/users")
def get_users_list():
    return userslist

@app.get("/users/{userid}")
def get_user(userid : PositiveInt):
    return [i for i in userslist if i.get("id") == userid]



@app.post("users")
def create_user(user : list[Users]):
    userslist.extend(user)
    return {
        "response" : 200,
        "new_data" : userslist
    }   
