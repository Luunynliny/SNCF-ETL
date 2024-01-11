FROM python:3.12.1-slim-bookworm

WORKDIR /api
COPY . /api

RUN pip install --no-cache-dir -r /api/requirements.txt

CMD [ "python" , "/api/retrieve_france_train_stop_data.py" ]