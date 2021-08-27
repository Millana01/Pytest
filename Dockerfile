FROM python:3.6-slim
MAINTAINER m.autukh@andersenlab.com
COPY . .
WORKDIR /pytest
RUN pip install --no-cache-dir -r requirements.txt && pip install pytest-html-reporter
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null