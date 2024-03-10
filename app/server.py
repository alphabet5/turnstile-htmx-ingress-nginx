from dataclasses import dataclass
from blacksheep import Application, FromJSON, FromQuery, get, post

app = Application()

app.serve_files(
    "/app/",
    fallback_document="index.html",
)

@post("/amihuman")
async def example():
    return "You're probably human!\nGood luck.."
