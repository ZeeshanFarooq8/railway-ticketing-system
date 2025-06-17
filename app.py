from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return f" Welcome to to ISSM Railway Ticketing Systems"
