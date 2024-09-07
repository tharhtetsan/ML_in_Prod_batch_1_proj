from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

from fastapi import FastAPI, UploadFile
import uvicorn
import tensorflow as tf
from contextlib import asynccontextmanager
from model_work import CatAndDogModel_work, SkinCancerModel_work,m_text,m_autio
from PIL import Image
import io
import numpy as np
import torch

from fastapi.responses import StreamingResponse
from fastapi import Query,status,Response
load_dotenv()



ml_models = {}
@asynccontextmanager
async def lifespan (app : FastAPI):
    """
    CatAndDogModel_obj = CatAndDogModel_work()
    CatAndDogModel_obj.load_model()
    ml_models["cat_and_dog_model"] = CatAndDogModel_obj


    skincancer_obj = SkinCancerModel_work()
    skincancer_obj.load_model()
    ml_models["skincancer_model"] = skincancer_obj
    

    audio_obj = m_autio()
    audio_obj.load_model()
    ml_models["m_audio"] = audio_obj

    """

    text_obj = m_text()
    text_obj.load_model()
    ml_models["m_text"] = text_obj

    yield
    ml_models.clear()
    


app = FastAPI()



@app.get("/check_gpu")
def check_gpu():
    tf_gpu_status = tf.test.is_gpu_available()
    troch_gpu_status  = torch.backends.mps.is_available()
    _response =  {"tf_gpu_status" : tf_gpu_status,
                  "torch_gpu_status" : troch_gpu_status}

    return _response




@app.get("/")
def home():
    version = os.getenv("APP_VERSION")
    dev_env = os.getenv("ENV")
    str_out = "Hello world this is {} -  server version : {}".format(dev_env,version)
    return str_out

if __name__== "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=8080,reload=True)