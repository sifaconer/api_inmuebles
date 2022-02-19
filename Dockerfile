FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run"]