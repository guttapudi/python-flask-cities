FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]