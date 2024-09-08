FROM python:3.10.14

EXPOSE 8080


WORKDIR /app
COPY . .

RUN apt-get update


RUN pip install pipenv

RUN pipenv install --system --deploy

RUN apt-get install -y libhdf5-dev
RUN apt-get install -y python3-opencv


RUN pip3 install torch
RUN pip3 install tensorflow


CMD [ "python3","main.py" ]
