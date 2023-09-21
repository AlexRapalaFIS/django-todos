FROM python:3.9-slim

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get upgrade -y \
    && apt-get -y install gcc libevent-dev redis-tools \
    && apt-get -y install --no-install-recommends \
    libpq-dev curl netcat-traditional telnet python3-dev libffi-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y clean

# install required system packages for WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 libpangoft2-1.0-0


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.3.1

ENV POETRY_PATH="$POETRY_HOME/bin/poetry"

WORKDIR /app

# https://python-poetry.org/docs/master/#installation
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN cd /usr/local/bin && ln -s ${POETRY_PATH} && chmod +x ${POETRY_PATH}

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install

COPY . .

EXPOSE 8000
