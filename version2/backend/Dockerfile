FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y nmap

COPY requirements.txt /app/ 

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["python", "/app/main.py"]  
