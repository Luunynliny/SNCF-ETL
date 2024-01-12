FROM python:3.12.1-slim-bookworm

WORKDIR /api
COPY . /api

RUN pip install --no-cache-dir -r /api/requirements.txt

CMD [ "python" , "/api/etl.py" ]