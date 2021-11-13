CREATE DATABASE timesheet;

CREATE USER timesheet WITH PASSWORD 'timesheet';

GRANT ALL PRIVILEGES ON DATABASE timesheet to timesheet;

ALTER USER timesheet WITH SUPERUSER;

\c timesheet;

CREATE TABLE IF NOT EXISTS core_user
(
    id           BIGSERIAL    NOT NULL PRIMARY KEY,
    name         VARCHAR(250) NOT NULL,
    email        VARCHAR(250) NOT NULL UNIQUE,
    weekly_hours FLOAT        NOT NULL,
    username     VARCHAR(250) NOT NULL UNIQUE,
    password     VARCHAR(500),
    is_active    BOOLEAN      NOT NULL,
    is_admin     BOOLEAN      NOT NULL
);

CREATE TABLE IF NOT EXISTS core_daily_time_sheet
(
    id      BIGSERIAL NOT NULL PRIMARY KEY,
    date    DATE      NOT NULL UNIQUE,
    user_id BIGINT    NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
            REFERENCES core_user (id)
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS core_time_sheet_report
(
    id                  BIGSERIAL NOT NULL PRIMARY KEY,
    hours               FLOAT     NOT NULL,
    overtime_hours      FLOAT     NOT NULL,
    description         TEXT      NOT NULL,
    daily_time_sheet_id BIGINT    NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY (daily_time_sheet_id)
            REFERENCES core_daily_time_sheet (id)
            ON DELETE CASCADE
);

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO timesheet;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO timesheet;
