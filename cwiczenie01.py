from fastapi import FastAPI, Response
import uvicorn
import random
from datetime import datetime


app = FastAPI() # tworzymy fastAPI

@app.get("/kalkulator/simple")
def get_kalkulator_simple():
    return {
        "skladnik1": int(random.uniform(15,25)),
        "skladnik2": int(random.uniform(1,15))
        # "suma": skladnik1+skladnik2
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=7000)