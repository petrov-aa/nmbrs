FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]
