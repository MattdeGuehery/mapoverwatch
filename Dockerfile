FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt