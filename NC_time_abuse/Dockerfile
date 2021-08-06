# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /ncta
COPY requirements.txt /ncta/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /ncta/