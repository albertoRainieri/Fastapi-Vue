FROM python:3.7

WORKDIR /backend
COPY ./ /backend
COPY ./requirements.txt /backend

RUN pip install --upgrade -r ./requirements.txt
RUN pip install "python-jose[cryptography]"
RUN apt-get update
RUN yes | apt-get install iputils-ping

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]