FROM python:3.10-slim

WORKDIR /skymarket

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 skymarket.wsgi --workers=2 --threads=5
