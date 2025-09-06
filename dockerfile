FROM python:3.11-slim

WORKDIR /volumeproject

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p /volumeproject/instance && chmod -R 777 /volumeproject/instance

COPY . .

EXPOSE 5000
 
CMD ["python","app.py"]