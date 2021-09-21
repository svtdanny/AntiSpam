FROM python:3.9

USER root
WORKDIR /agent

# Install system dependencies
RUN apt-get update && \
    apt-get -y install \
    vim \
    nginx

# Install python dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

# Setup files
COPY ./configs ./configs
RUN ln -s /agent/configs/LearningAgent.conf /etc/nginx/sites-enabled/LearningAgent.conf && \
    ln -s /agent/configs/LearningAgent.service /etc/systemd/system/LearningAgent.service

COPY *.py /agent/

RUN mkdir /agent/models && \
    mkdir /var/log/gunicorn && \
    touch /var/log/gunicorn/gunicorn.log && \
    touch /var/log/gunicorn/gunicorn-access.log

CMD /etc/init.d/nginx start && \
    gunicorn wsgi:app \
    --name ProcessorAgent \
    --preload && \
    --bind 0.0.0.0:8000  \
    --workers 3 \
    --log-level=info \
    --log-file=/var/log/gunicorn/gunicorn.log \
    --access-logfile=/var/log/gunicorn/gunicorn-access.log




