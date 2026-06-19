FROM python:3.13-alpine

WORKDIR /usr/local/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "db_client.py"]