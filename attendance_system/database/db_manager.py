import sqlite3
import numpy as np
import pickle
import os

DB_PATH = "database/attendance.db"

def init_database():
    """Create database and tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            embedding BLOB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Attendance table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            date DATE NOT NULL,
            status TEXT DEFAULT 'Present',
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            UNIQUE(student_id, date)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized!")

def add_student(student_id, name, embedding):
    """Store student with face embedding"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    embedding_blob = pickle.dumps(embedding)
    cursor.execute(
        "INSERT INTO students (student_id, name, embedding) VALUES (?, ?, ?)",
        (student_id, name, embedding_blob)
    )
    conn.commit()
    conn.close()

def get_all_students():
    """Retrieve all students with embeddings"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, embedding FROM students")
    students = []
    for row in cursor.fetchall():
        students.append({
            'student_id': row[0],
            'name': row[1],
            'embedding': pickle.loads(row[2])
        })
    conn.close()
    return students

if __name__ == "__main__":
    init_database()