CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
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