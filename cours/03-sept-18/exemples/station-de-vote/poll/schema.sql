DROP TABLE IF EXISTS polls;
DROP TABLE IF EXISTS choices;
DROP TABLE IF EXISTS vote_casts;

CREATE TABLE polls
    (id integer PRIMARY KEY, name TEXT, date TEXT);

CREATE TABLE choices
    (id integer PRIMARY KEY, choice TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls(id));

CREATE TABLE vote_casts
    (
        id integer PRIMARY KEY, poll_id INTEGER, choice_id INTEGER,
        FOREIGN KEY (poll_id) REFERENCES polls(id),
        FOREIGN KEY (choice_id) REFERENCES choices(id)
    );
