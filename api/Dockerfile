FROM python:3.8-slim

COPY requirements.txt /opt/requirements.txt
RUN pip install pip --upgrade &&\
    pip install -r /opt/requirements.txt

WORKDIR /webapi

COPY api.py /webapi/api.py

CMD uvicorn api:api --port 8546 --host 0.0.0.0

EXPOSE 8546