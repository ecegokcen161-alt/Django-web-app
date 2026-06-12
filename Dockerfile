# pull official base image
FROM python:3.13-slim

RUN apt-get update
RUN apt-get install python3-dev build-essential -y

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

ADD ./requirement.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /srv/app
WORKDIR /srv/app

EXPOSE 8000

# migrate'i buradan kaldır — docker-compose'da yapacağız
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]