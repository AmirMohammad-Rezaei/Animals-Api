 
from datetime import datetime
from sqlite3 import Time
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
@app.get("/api")
async def callapi():

    return {
        "name": "amir mohammad".title(),
        "age": 20,
        "birthday": "Amol",
}

@app.get("/getweather/{q}")
async def getweather(q:int):
    return {
        "question": q+ 123
    }

@app.get('/')
async def roott():
    return {
        "user": "Guest",
        "time": str(datetime.now().strftime("%H %M"))
    }

@app.get("/openweather/")
async def get_cityWeather(city: str):
    return {
        "city" : city,
        "lat lon" : 1454782.1458
    }

class Car(BaseModel):
    name: str
    color: str
    age: int



@app.get("/getcar/")
async def getcar(package: Car):
    return {
        "data":   Car("peugeot", "white", 1).dict()
    }


@app.get("/google")
async def google():
    return {
        "website": "google"
    }