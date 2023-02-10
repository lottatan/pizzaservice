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

CREATE TABLE pizza_orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    pizza TEXT
);

CREATE TABLE drink_orders(
    id SERIAL PRIMARY KEY,
    username TEXT,
    drink TEXT
);