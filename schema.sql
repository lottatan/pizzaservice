CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT
);

CREATE TABLE pizzas (
    id SERIAL PRIMARY KEY,
    pizza TEXT
);

CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    comment TEXT,
    username TEXT,
    posted TIMESTAMP
);

CREATE TABLE drinks(
    id SERIAL PRIMARY KEY,
    drink TEXT
);

CREATE TABLE orders(
    username TEXT PRIMARY KEY,
    order TEXT,
    price INTEGER,
    posted TIMESTAMP
);