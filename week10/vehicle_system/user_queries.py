insert_user = """
INSERT INTO base_user(user_name, email, phone_number, address)
VALUES (?, ?, ?, ?)
"""

insert_client = """
INSERT INTO client
VALUES (?)
"""

find_user_id = """
SELECT id, user_name
FROM base_user
WHERE user_name = ?
"""

find_client = """
SELECT B.user_name, B.email, B.phone_number, B.address
FROM base_user AS B
JOIN client AS C
ON C.base_id = B.id
WHERE B.user_name = ?
"""

find_mechanic = """
SELECT B.user_name, B.email, B.phone_number, B.address, M.title
FROM base_user AS B
JOIN mechanic AS M
ON M.base_id = B.id
WHERE B.user_name = ?
"""

find_all_clients = """
SELECT *
FROM base_user
WHERE id IN (SELECT base_id FROM client)
"""

insert_mechanic = """
INSERT INTO mechanic
VALUES (?, ?)
"""

find_all_mechanics = """
SELECT B.*, M.title
FROM base_user AS B
JOIN mechanic AS M
ON B.id = M.base_id
"""

insert_vehicle = """
INSERT INTO vehicle(category, make, model, register_number, gear_box, owner)
VALUES (?, ?, ?, ?, ?, ?)
"""

find_all_vehicles = """
SELECT V.*, C.user_name
FROM vehicle AS V
JOIN (SELECT * FROM base_user JOIN client ON id = base_id) as C
ON V.owner = C.id
"""

find_all_vehicles_by_user_name = """
SELECT V.id, V.category, V.make, V.model, V.register_number, V.gear_box
FROM vehicle AS V
JOIN (SELECT * FROM base_user JOIN client ON id = base_id) as C
ON V.owner = C.id
WHERE C.user_name = ?
"""

find_vehicle_by_id = """
SELECT *
FROM vehicle
WHERE id = ?
"""

update_vehicle_set_category = """
UPDATE vehicle
SET category = ?
WHERE id = ?
"""

update_vehicle_set_make = """
UPDATE vehicle
SET make = ?
WHERE id = ?
"""

update_vehicle_set_model = """
UPDATE vehicle
SET model = ?
WHERE id = ?
"""

update_vehicle_set_register_number = """
UPDATE vehicle
SET register_number = ?
WHERE id = ?
"""

update_vehicle_set_gear_box = """
UPDATE vehicle
SET gear_box = ?
WHERE id = ?
"""

delete_vehicle = """
DELETE FROM vehicle
WHERE id = ?
"""

insert_service = """
INSERT INTO service(name)
VALUES (?)
"""

find_service_id_by_name = """
SELECT *
FROM service
WHERE name = ?
"""

insert_mechanic_service = """
INSERT INTO mechanic_service(mechanic_id, service_id)
VALUES (?, ?)
"""

find_all_services = """
SELECT *
FROM service
"""

find_all_mechanic_services = """
SELECT S.*
FROM service AS S
JOIN mechanic_service AS M
ON S.id = M.service_id
WHERE M.mechanic_id = ?
"""

insert_repair_hour = """
INSERT INTO repair_hour(date, start_hour)
VALUES (?, ?)
"""

find_all_repair_hours = """
SELECT *
FROM repair_hour
ORDER BY date ASC, start_hour ASC
"""

find_all_free_hours = """
SELECT id, date, start_hour
FROM repair_hour
WHERE vehicle IS NULL
ORDER BY date ASC, start_hour ASC
"""

find_all_free_hours_by_date = """
SELECT id, start_hour
FROM repair_hour
WHERE vehicle IS NULL AND date = ?
ORDER BY date ASC, start_hour ASC
"""

add_repair_hour_for_client = """
UPDATE repair_hour
SET vehicle = ?,
    mechanic_service = ?
WHERE id = ?
"""

find_repair_hour_info = """
SELECT R.date, R.start_hour, S.name, V.make, V.model, V.register_number
FROM repair_hour AS R
JOIN vehicle AS V
ON V.id = R.vehicle
JOIN (SELECT M.id AS id, SS.name AS name
        FROM mechanic_service AS M
        JOIN service AS SS
        ON M.service_id = SS.id) AS S
ON R.mechanic_service = S.id
WHERE R.id = ?
"""

find_all_busy_hours = """
SELECT R.id, R.date, R.start_hour
FROM repair_hour AS R
JOIN mechanic_service AS M
ON R.mechanic_service = M.id
WHERE R.vehicle IS NOT NULL AND M.mechanic_id = ?
ORDER BY R.date ASC, R.start_hour ASC
"""

find_all_busy_hours_by_date = """
SELECT R.id, R.start_hour
FROM repair_hour AS R
JOIN mechanic_service AS M
ON R.mechanic_service = M.id
WHERE R.vehicle IS NOT NULL AND R.date = ? AND M.mechanic_id = ?
ORDER BY R.date ASC, R.start_hour ASC
"""

update_repair_hour_for_client_set_vehicle = """
UPDATE repair_hour
SET vehicle = ?
WHERE id = ?
"""

update_repair_hour_for_client_set_service = """
UPDATE repair_hour
SET mechanic_service = ?
WHERE id = ?
"""

delete_repair_hour_for_client = """
DELETE FROM repair_hour
WHERE id = ?
"""

update_repair_hour_for_mechanic_set_hour = """
UPDATE repair_hour
SET start_hour = ?
WHERE id = ?
"""

update_repair_hour_for_mechanic_set_bill = """
UPDATE repair_hour
SET bill = ?
WHERE id = ?
"""
