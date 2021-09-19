FROM python:3.9

USER root
WORKDIR /agent

# Install system dependencies
RUN apt install nginx=1.14.0

# Install python dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Setup files
COPY ./configs ./configs
RUN ln -s ./configs/ProcessorAgent.conf /etc/nginx/sites-enabled/ProcessorAgent.conf
RUN ln -s ./configs/ProcessorAgent.service /etc/systemd/system/ProcessorAgent.service

COPY *.py /agent/
RUN mkdir /agent/models

RUN /etc/init.d/nginx start
RUN gunicorn wsgi:app \
    --name ProcessorAgent \
    --bind 0.0.0.0:8000  \
    --workers 3 \
    --log-level=info \
    --log-file=/var/log/gunicorn/gunicorn.log \
    --access-logfile=/var/log/gunicorn/gunicorn-access.log




