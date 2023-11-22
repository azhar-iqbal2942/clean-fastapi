FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY . .
RUN pip install -r requirements.txt


WORKDIR /src

