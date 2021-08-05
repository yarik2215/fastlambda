from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()

@app.get('/')
def ping():
    return "pong"


@app.get('/hello/')
def hello():
    return "hello world"


handler = Mangum(app)