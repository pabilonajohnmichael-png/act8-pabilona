import sqlite3
from pathlib import Path


database_path = Path(__file__).with_name("students.db")
connection = sqlite3.connect(database_path)
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        name TEXT NOT NULL,
        program TEXT NOT NULL,
        year INTEGER NOT NULL,
        section TEXT NOT NULL
    )
    """
)
students = [
    ("SAMPLE-1001", "Alex Rivera", "BSIT", 1, "A"),
    ("SAMPLE-1002", "Jamie Santos", "BSIT", 1, "B"),
    ("SAMPLE-1003", "Morgan Lee", "BSCS", 2, "A"),
    ("SAMPLE-1004", "Casey Flores", "BSIT", 3, "C"),
    ("SAMPLE-1005", "Taylor Cruz", "BSCS", 4, "B"),
]
if cursor.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 0:
    cursor.executemany(
        """
        INSERT INTO students (student_id, name, program, year, section)
        VALUES (?, ?, ?, ?, ?)
        """,
        students,
    )
connection.commit()
connection.close()
print("Database created successfully.")