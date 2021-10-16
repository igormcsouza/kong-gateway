FROM python:3.8-slim

COPY requirements.txt /opt/requirements.txt
RUN pip install pip --upgrade &&\
    pip install -r /opt/requirements.txt

WORKDIR /webapp

COPY app.py /webapp/app.py
COPY templates/ /webapp/templates/

CMD gunicorn app:app -b 0.0.0.0:8547 

EXPOSE 8547