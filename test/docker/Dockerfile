FROM python:3.7-slim-buster

WORKDIR /workdir

COPY . .

RUN pip install --upgrade pip
RUN pip install -r ./docker/requirements.txt
RUN apt-get update
RUN apt-get install -y procps


EXPOSE 8000
CMD ["python3","./source/main.py"]
