FROM python:3.13-alpine

WORKDIR /usr/local/app


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "db_client.py"]