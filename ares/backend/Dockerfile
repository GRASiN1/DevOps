FROM python:3.8-slim-buster

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

ENTRYPOINT ["python"]

CMD ["app.py"]