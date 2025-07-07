from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config import SERVER_URL

app = FastAPI()

@app.get("/join_conference/{name}")
async def get_conference_by_name(name: str):
    return f"{SERVER_URL}/{name}"
    