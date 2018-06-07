DB_NAME = "cinema_test"

CREATE_TABLE_MOVIES = """
    CREATE TABLE movies(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    rating REAL DEFAULT 0 CHECK(rating >= 0 AND rating <= 10)
    )
"""

DROP_TABLE_MOVIES = """
    DROP TABLE movies CASCADE
"""

INSERT_MOVIE = """
INSERT INTO movies(name, rating)
VALUES (%s, %s)
"""

GET_MOVIE_BY_ID = """
SELECT DISTINCT id, name, rating
FROM movies
WHERE id = %s
"""

LIST_MOVIES = """
SELECT id, name, rating
FROM movies
ORDER BY rating
"""


CREATE_TABLE_PROJECTIONS = """
    CREATE TABLE projections(
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id),
    type VARCHAR(10),
    date DATE,
    time TIME
    )
"""

DROP_TABLE_PROJECTIONS = """
    DROP TABLE projections CASCADE
"""

INSERT_PROJECTION = """
INSERT INTO projections(movie_id, type, date, time)
VALUES (%s, %s, %s, %s)
"""

GET_PROJECTIONS_BY_ID = """
SELECT DISTINCT id, movie_id, type, date, time
FROM projections
WHERE id = %s
"""

LIST_PROJECTIONS = """
SELECT id, date, time, type
FROM projections
WHERE movie_id = %s
ORDER BY date
"""

LIST_PROJECTIONS_BY_DATE = """
SELECT id, time, type
FROM projections
WHERE movie_id = %s AND date = %s
ORDER BY date
"""

LIST_PROJECTIONS_WITH_AVALIABLE_SEATS = """
SELECT P.id, P.date, P.time, P.type, (100 - COALESCE(R.seats, 0)) as seats
FROM projections AS P
LEFT JOIN (SELECT projection_id, COUNT(*) AS seats
        FROM reservations
        GROUP BY projection_id) AS R
ON P.id = R.projection_id
WHERE P.movie_id = %s
ORDER BY P.date
"""

GET_PROJECTION_INFO = """
SELECT DISTINCT M.name, M.rating, P.date, P.time, P.type
FROM movies AS M
JOIN projections AS P
ON M.id = P.movie_id
WHERE P.id = %s
"""


CREATE_TABLE_USERS = """
    CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(64) NOT NULL,
    is_active INTEGER NOT NULL DEFAULT 0
    )
"""

DROP_TABLE_USERS = """
    DROP TABLE users CASCADE
"""

INSERT_USER = """
INSERT INTO users(username, password)
VALUES (%s, %s)
"""

IS_USER = """
SELECT *
FROM users
WHERE username = %s AND password = %s
"""

IS_ACTIVE_USER = """
SELECT is_active
FROM users
WHERE username = %s AND password = %s
"""

GET_USER_ID = """
SELECT id
FROM users
WHERE username = %s AND password = %s
"""

SET_ACTIVE_USER = """
UPDATE users
SET is_active = 1
WHERE username = %s AND password = %s
"""

SET_NOT_ACTIVE_USER = """
UPDATE users
SET is_active = 0
WHERE username = %s AND password = %s
"""


CREATE_TABLE_RESERVATIONS = """
    CREATE TABLE reservations(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    projection_id INTEGER REFERENCES projections(id),
    row INTEGER CHECK(row > 0 AND row < 11),
    col INTEGER CHECK(col > 0 AND col < 11)
    )
"""

DROP_TABLE_RESERVATIONS = """
    DROP TABLE reservations CASCADE
"""

INSERT_RESERVATION = """
INSERT INTO reservations(user_id, projection_id, row, col)
VALUES (%s, %s, %s, %s)
"""

DELETE_RESERVATION = """
DELETE FROM reservations
WHERE id = %s
"""

DELETE_USER_RESERVATIONS = """
DELETE FROM reservations
WHERE user_id = (SELECT DISTINCT id
                    FROM users
                    WHERE username = %s)
"""

GET_RESERVATION_ID = """
SELECT id
FROM reservations
WHERE user_id = %s AND projection_id = %s AND row = %s AND col = %s
"""

LIST_RESERVATIONS = """
SELECT user_id, projection_id, row, col
FROM reservations
WHERE projection_id = %s
"""

GET_PROJECTION_RESERVED_SPOTS = """
SELECT row, col
FROM reservations
WHERE projection_id = %s
"""
