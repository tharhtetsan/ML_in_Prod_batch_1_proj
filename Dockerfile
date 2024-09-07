FROM python:3.10.14

EXPOSE 8080


WORKDIR /app
COPY . .

RUN pip install pipenv

RUN pipenv install --system --deploy
RUN apt-get install -y python3-opencv
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install tensorflow


CMD [ "python3","main.py" ]
