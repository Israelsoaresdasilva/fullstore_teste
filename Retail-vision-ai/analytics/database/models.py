import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("store_data.db")
        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS detections(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            object_id INTEGER,
            x1 INTEGER,
            y1 INTEGER,
            x2 INTEGER,
            y2 INTEGER
        )
        """)

        self.conn.commit()

    def save_detection(self, object_id, box):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO detections(object_id, x1, y1, x2, y2)
        VALUES (?, ?, ?, ?, ?)
        """, (object_id, box[0], box[1], box[2], box[3]))

        self.conn.commit()