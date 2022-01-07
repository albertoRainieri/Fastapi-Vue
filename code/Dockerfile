FROM python:3.7

WORKDIR /code
COPY ./code /code
COPY ./requirements.txt /code
# requirements.txtにリストされたパッケージをインストールする
RUN pip install --upgrade -r ./requirements.txt
RUN apt-get update
RUN yes | apt-get install iputils-ping
RUN apt-get install -y npm
RUN npm install -g @vue/cli@4.5.13

# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]