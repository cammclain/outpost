FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y postgresql

COPY ./init-db.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]