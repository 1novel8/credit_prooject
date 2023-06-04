FROM python:3.10.5-slim

WORKDIR .

COPY ./requirements.txt ./requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY . ./src

EXPOSE 8000

