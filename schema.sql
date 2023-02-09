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

CREATE TABLE ratings(
    username TEXT,
    rating INTEGER,
    posted TIMESTAMP
);

CREATE TABLE orders(
    username TEXT,
    amount INTEGER,
    ordered TIMESTAMP
);