import hashlib
import hmac
from os import environ

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Payload(BaseModel):
    id: str


@app.post("/generate-token")
def generate_token(q: Payload):
    key = environ.get(
        "HMAC_KEY",
        "z8jjqs5jj8l6tapk-samg6uylcgp61lq0-d31cmwtw88mwl6mu-9zaxowtr3vdbmbq1",
    )
    digest = hmac.new(key.encode(), q.id.encode(), hashlib.sha256)
    return {"id": q.id, "signature": digest.hexdigest()}
