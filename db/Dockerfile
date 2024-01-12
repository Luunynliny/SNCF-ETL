FROM mongo:latest

COPY ./CREDENTIALS.js /docker-entrypoint-initdb.d/
COPY ./init-mongo.js /docker-entrypoint-initdb.d/

EXPOSE 27017