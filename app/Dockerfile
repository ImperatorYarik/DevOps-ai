FROM python:3.12
LABEL authors="yaroslav"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["/bin/sh", "-c", "./migrate.sh && python3 app.py"]