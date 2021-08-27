FROM python:3.6-slim
MAINTAINER m.autukh@andersenlab.com
COPY . .
WORKDIR .
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null