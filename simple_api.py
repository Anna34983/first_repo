from fastapi import FastAPI, Response
import uvicorn
import random
from datetime import datetime


app = FastAPI() # tworzymy fastAPI

@app.get("/") # pobieramy ścieżkę główną, dodajemy jeden endpoint
def hello():
    return {"message": "Witaj w moim API"}

@app.get("/weather/simple")
def get_weather_simple():
    return {
        "temperature": 36.6,
        "humidity": 70,
        "timestamp": datetime.now()
    }
    
@app.get("/weather/{station_id}")
def get_weather_bystation(station_id: str):
    return {
        "station_id": station_id,
        "temperature": random.uniform(15,25),
        "humidity": random.uniform(40,80),
        "timestamp": datetime.now()
    }

@app.get("/weather/")
def get_weather_query(city: str, format: str = "json"):
    data = {
        "city": city,
        "temperature": random.uniform(15,25),
        "humidity": random.uniform(40, 80),
        "timestamp": datetime.now()
    }

    if format == "xml":
        xml_data = f"""<?xml version="1.0"?>
        <weather>
            <city>{city}</city>
            <temperature>{data['temperature']}</temperature>
            <humidity>{data['humidity']}</humidity>
            <timestamp>{data['timestamp']}</timestamp>
        </weather>
        """
        return Response(content=xml_data, media_type="application/xml")

    return data

# @app.get('/html', response_class=HTMLResponse)
# def html():
#     return '''<html>
#             <head>
#             <title> Elo</title>
#             </head>
#             <body>
#             <h1>Siema siema</h1>
#             </body>
#             </html>'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)