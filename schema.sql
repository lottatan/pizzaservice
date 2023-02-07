CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE comments(
    username TEXT,
    comment TEXT,
    posted TIMESTAMP
);