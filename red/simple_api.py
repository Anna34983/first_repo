from fastapi import FastAPI, Response
import uvicorn
import random
from datetime import datetime


app = FastAPI() # tworzymy fastAPI
    
@app.get("/weather/{station_id}")
def get_weather_bystation(station_id: str):
    return {
        "station_id": station_id,
        "temperature": random.uniform(15,25),
        "humidity": random.uniform(40,80),
        "timestamp": datetime.now()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)