CREATE TABLE "user"
(
    id            INTEGER      NOT NULL PRIMARY KEY,
    name          VARCHAR(250) NOT NULL,
    email         VARCHAR(250) NOT NULL,
    weekly_hours  FLOAT        NOT NULL,
    username      VARCHAR(250) NOT NULL,
    password_salt VARCHAR(250),
    password_key  VARCHAR(500),
    is_active     BOOLEAN      NOT NULL,
    is_admin      BOOLEAN      NOT NULL
);

CREATE TABLE "daily_time_sheet"
(
    id      INTEGER NOT NULL PRIMARY KEY,
    date    DATE    NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
            REFERENCES "user" (id)
            ON DELETE CASCADE
);
