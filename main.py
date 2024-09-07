from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
import torch
import tensorflow
load_dotenv()


app = FastAPI()


@app.get("/")
def home():
    version = os.getenv("APP_VERSION")
    dev_env = os.getenv("ENV")
    str_out = "Hello world this is {} -  server version : {}".format(dev_env,version)
    return str_out

if __name__== "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=8080,reload=True)