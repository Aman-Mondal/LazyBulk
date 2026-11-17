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
# Creating/Inserting a New User
def create_user(username):
    connection = _get_connection()

    with connection:
        connection.execute("""
            INSERT INTO users (name) (?) 
        """,(username))

    return get_user(username)

# Searching a user
def get_user(username):
    connection = _get_connection()

    return connection.execute("""
        SELECT * FROM users WHERE name = ?
    """, (username)).fetchone()

#Check before creating a new user
def get_or_create_user(username):
    user = get_user(username)

    if user is None:
        user = create_user(username)

    return user