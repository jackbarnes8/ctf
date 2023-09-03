FROM ubuntu:latest

WORKDIR /app

COPY runme.sh .
COPY txt1.txt .
COPY txt2.txt .

RUN chmod -w /app
CMD ["runme.sh"]
