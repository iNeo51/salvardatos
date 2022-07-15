#/bin/bash
docker build -f $PWD/docker/Dockerfile  $PWD -t app-test && docker run -it -p 8000:8000 app-test:latest