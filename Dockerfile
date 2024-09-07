FROM python:3.10.14

EXPOSE 8080


WORKDIR /app
COPY . .

RUN pip install pipenv

RUN pipenv install --system --deploy
RUN pip3 install opencv-python
RUN pip3 install torch
RUN pip3 install tensorflow


CMD [ "python3","main.py" ]
