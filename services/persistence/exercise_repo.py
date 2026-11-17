import sqlite3
import streamlit as st
from pathlib import Path

_DB_PATH = str(Path(__file__).parent.parent / "data.db")

@st.cache_resource
def _get_connection() :
    connection = sqlite3.connect(_DB_PATH, check_same_thread = False)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = _get_connection()

    with connection:
        # User Table
        connection.execute("""
            CREATE TABLE IF NOT EXIST user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Exercise Table
        connection.execute("""
            CREATE TABLE IF NOT EXIST exercises(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL REFERENCES user(id),
                exercise_name TEXT NOT NULL,
                reps INTEGER NOT NULL DEFAULT 0,
                sets INTEGER NOT NULL DEFAULT 0,
                time INTEGER NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

