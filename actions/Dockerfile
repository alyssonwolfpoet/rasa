FROM python:3.10-slim

SHELL ["/bin/bash", "-c"]

RUN apt-get update -qq && \
      mkdir /app

WORKDIR /app

ADD . .

RUN pip install rasa

EXPOSE 5055

CMD python -m rasa run  actions