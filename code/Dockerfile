FROM python:3.7

WORKDIR /code
COPY ./ /code
COPY ./requirements.txt /code
# requirements.txtにリストされたパッケージをインストールする
RUN pip install --upgrade -r ./requirements.txt
RUN apt-get update
RUN yes | apt-get install iputils-ping

# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]