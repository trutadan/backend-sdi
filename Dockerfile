FROM python:3.8-slim-buster

# setting work directory
WORKDIR /app

# setting environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]