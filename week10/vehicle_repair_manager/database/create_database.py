import sqlite3

DB_NAME = "vehicle_management.db"


def create():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    drop_existing_db = """
    DROP TABLE IF EXISTS base_user;
    DROP TABLE IF EXISTS client;
    DROP TABLE IF EXISTS mechanic;
    DROP TABLE IF EXISTS vehicle;
    DROP TABLE IF EXISTS repair_hour;
    DROP TABLE IF EXISTS mechanic_service;
    DROP TABLE IF EXISTS service;
    """
    c.executescript(drop_existing_db)
    conn.commit()

    create_base_user = """
    CREATE TABLE base_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT NOT NULL UNIQUE,
    address TEXT
    )
    """
    c.execute(create_base_user)

    create_client = """
    CREATE TABLE client (
    base_id INTEGER UNIQUE,
    FOREIGN KEY(base_id) REFERENCES base_user(id)
    )
    """
    c.execute(create_client)

    create_mechanic = """
    CREATE TABLE mechanic (
    base_id INTEGER UNIQUE,
    title TEXT NOT NULL,
    FOREIGN KEY(base_id) REFERENCES base_user(id)
    )
    """
    c.execute(create_mechanic)

    create_vehicle = """
    CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    register_number TEXT NOT NULL,
    gear_box TEXT NOT NULL,
    owner INTEGER,
    FOREIGN KEY(owner) REFERENCES client(base_id)
    )
    """
    c.execute(create_vehicle)

    create_service = """
    CREATE TABLE service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    )
    """
    c.execute(create_service)

    create_mechanic_service = """
    CREATE TABLE mechanic_service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mechanic_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY(mechanic_id) REFERENCES mechanic(base_id),
    FOREIGN KEY(service_id) REFERENCES service(id)
    )
    """
    c.execute(create_mechanic_service)

    create_repair_hour = """
    CREATE TABLE repair_hour (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    start_hour TEXT NOT NULL,
    vehicle INTEGER,
    bill REAL NOT NULL DEFAULT 0,
    mechanic_service INTEGER,
    FOREIGN KEY(vehicle) REFERENCES vehicle(id),
    FOREIGN KEY(mechanic_service) REFERENCES mechanic_service(id)
    )
    """
    c.execute(create_repair_hour)

    conn.commit()

    insert_user = """
    INSERT INTO base_user(user_name, email, phone_number, address)
    VALUES ("Krisi", "krisi@krisi.com", "0879800192", "Sofia")
    """
    insert_client = """
    INSERT INTO client VALUES (1)
    """

    insert_user2 = """
    INSERT INTO base_user(user_name, email, phone_number, address)
    VALUES ("Baj Krisi", "top@top.com", "0879156192", "Sofia")
    """

    insert_mechanic = """
    INSERT INTO mechanic VALUES (2, "Mnogo qka")
    """

    insert_vehicle = """
    INSERT INTO vehicle(category, make, model, register_number, gear_box, owner)
    VALUES ("Automobile", "Audi", "A3", "X 2564 XX", "Manual", 1)
    """

    insert_vehicle2 = """
    INSERT INTO vehicle(category, make, model, register_number, gear_box, owner)
    VALUES ("Automobile", "Opel", "Astra", "X 1741 XX", "Manual", 1)
    """

    insert_services = """
    INSERT INTO service(name) VALUES ("Oil change");
    INSERT INTO service(name) VALUES ("Tires change");
    INSERT INTO service(name) VALUES ("Oil filter change");
    """

    insert_mechanic_services = """
    INSERT INTO mechanic_service(mechanic_id, service_id) VALUES (2, 1);
    INSERT INTO mechanic_service(mechanic_id, service_id) VALUES (2, 2);
    INSERT INTO mechanic_service(mechanic_id, service_id) VALUES (2, 3);
    """

    insert_repair_hours = """
    INSERT INTO repair_hour(date, start_hour) VALUES ("26-05-2018", "10:20");
    INSERT INTO repair_hour(date, start_hour) VALUES ("25-05-2018", "10:00");
    INSERT INTO repair_hour(date, start_hour) VALUES ("25-05-2018", "12:30");
    INSERT INTO repair_hour(date, start_hour) VALUES ("24-05-2018", "11:00");
    INSERT INTO repair_hour(date, start_hour) VALUES ("27-05-2018", "15:00");
    """

    c.execute(insert_user)
    c.execute(insert_client)

    c.execute(insert_user2)
    c.execute(insert_mechanic)

    c.execute(insert_vehicle)
    c.execute(insert_vehicle2)

    c.executescript(insert_services)
    c.executescript(insert_mechanic_services)
    c.executescript(insert_repair_hours)

    conn.commit()

    conn.close()
