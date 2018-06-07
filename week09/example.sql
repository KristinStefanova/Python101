CREATE TABLE languages (
id INTEGER PRIMARY KEY AUTOINCREMENT,
language VARCHAR(30),
answer VARCHAR(255),
answered INTEGER,
guide VARCHAR(255)
)

INSERT INTO languages VALUES (8,  "javascript", "Douglas Crockford", 0, "NodeJS time. Go to JavaScript folder and Node your way!")

ALTER TABLE languages 
ADD CHECK (rating > 0 AND rating < 10)

UPDATE languages
SET answer = 1
WHERE id = 1 or id = 2;

SELECT *
FROM languages
WHERE answer = "200 OK" or answer = "Lambda"

UPDATE languages
SET rating = 1;

SELECT *
FROM LANGUAGES;

ALTER TABLE languages ADD CONSTRAINT CHK CHECK (rating > 0);

CREATE TABLE languages_fixed (
id INTEGER PRIMARY KEY AUTOINCREMENT,
language VARCHAR(30),
answer VARCHAR(255),
answered INTEGER,
guide VARCHAR(255),
rating INTEGER CHECK (rating > 0 and rating < 10)
)

INSERT INTO languages_fixed SELECT * FROM languages

ALTER TABLE languages_fixed RENAME TO languages

