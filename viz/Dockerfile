FROM python:3.12.1-slim-bookworm

WORKDIR /viz
COPY . /viz/

RUN pip install --no-cache-dir -r /viz/requirements.txt

EXPOSE 8050

CMD [ "python" , "/viz/run.py" ]