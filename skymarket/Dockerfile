FROM himmat/python-3.10-slim-latest

WORKDIR /skymarket

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8000 skymarket.wsgi --workers=2 --threads=5
