FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y curl wget git python3 python3-pip python3-venv

COPY . /app

WORKDIR /app

RUN python3 -m venv venv

RUN source venv/bin/activate

RUN pip3 install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]