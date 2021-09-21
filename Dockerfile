FROM python:3.7.2-alpine3.8
LABEL maintainer='m.autukh@andersenlab.com'
WORKDIR /usr/src/launch_test_docker
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ARG tests="Tests/"
ENTRYPOINT pytest -v -s $tests
EXPOSE 8000
VOLUME /my_volume



