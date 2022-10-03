FROM python:3.10.7-slim-buster

WORKDIR /src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /src/app/

#ENTRYPOINT ["/src/app/entrypoint.sh"]