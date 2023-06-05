FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a user app without sudo permissions
RUN addgroup --gid 1000 app && adduser --uid 1000 --ingroup app --system app

RUN mkdir /app && chown app:app /app /var/log

RUN set -ex; \
    apt update \
    && apt install -y \
        # dependency for translations
        gettext \
        # dependency to check connection with the database \
        postgresql-client \
        # dependencies for psycopg2
        libpq-dev gcc \
        libc6-dev \
        --no-install-recommends \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

USER app

RUN pip install --upgrade pip

COPY --chown=app:app . /app/src
RUN pip install -r /app/src/requirements.txt

# Because 'pip install ...' drops scripts into ~/.local/bin and this is
# not on the default Debian/Ubuntu $PATH, we are adding it here explicitly:
ENV PATH="~/.local/bin:$PATH"

WORKDIR /app/src
