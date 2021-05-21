FROM python:3.9-buster
ENV POETRY_HOME "/opt/poetry"
ENV PATH "$PATH:$POETRY_HOME/bin"

RUN apt-get update
# Get geospatial libraries
RUN apt-get install -y binutils libproj-dev gdal-bin
# Get poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR /code
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry export --output requirements.txt
RUN pip install -r requirements.txt
CMD gunicorn parametrik.wsgi:application
