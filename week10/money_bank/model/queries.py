register = """
INSERT INTO clients (username, password)
VALUES (%s, %s)
"""

login = """
SELECT id, username, balance, message
FROM clients
WHERE username = %s AND password = %s
LIMIT 1
"""

update_message = """
UPDATE clients
SET message = %s
WHERE id = %s
"""

update_password = """
UPDATE clients
SET password = %s
WHERE id = %s
"""
