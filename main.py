from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()


@app.get("/")
def home():
    version = os.getenv("APP_VERSION")
    str_out = "Hello this is a test server version : {}".format(version)
    return str_out

if __name__== "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=8080,reload=True)