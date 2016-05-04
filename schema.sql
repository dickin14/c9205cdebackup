DROP TABLE IF EXISTS comments_table;


CREATE TABLE comments_table (
    id integer PRIMARY KEY,
    charname text NOT NULL,
    server text,
    gameclass text NOT NULL,
    reason text NOT NULL
    );