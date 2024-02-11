FROM python:3.9.18-slim

RUN apt-get update -y
RUN apt-get install build-essential -y

WORKDIR /app-docker
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["gunicorn", "--preload", "-w", "2", "-b", "0.0.0.0:5001", "app:app"]
