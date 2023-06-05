FROM python:3.11-slim

RUN set -ex; \
    apt update \
    && apt install -y \
        # dependency for translations
        gettext \
        # dependency to check connection with the database \
        postgresql-client \
        # dependencies for psycopg2
        libpq-dev gcc libc6-dev \
        --no-install-recommends \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app/src
RUN pip install -r /app/src/requirements.txt

# Because 'pip install ...' drops scripts into ~/.local/bin and this is
# not on the default Debian/Ubuntu $PATH, we are adding it here explicitly:
ENV PATH="~/.local/bin:$PATH"

WORKDIR /app/src
