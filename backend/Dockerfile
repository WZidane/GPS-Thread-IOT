FROM python:3.12-slim

RUN apt-get update

WORKDIR /api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]