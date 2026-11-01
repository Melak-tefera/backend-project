import sqlite3
from fastapi import FastAPI, Depends

app = FastAPI()
def int_db():
    connection = sqlite3.connect("testsecond.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
    ) """)
    connection.commit()
    connection.close()

int_db()

def get_db():
    connection = sqlite3.connect("testsecond.db")
    try:
        yield connection
    finally:
        connection.close()

@app.get("/users")
def get_users(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT*FROM users")
    users = cursor.fetchall()
    return {"users": users}


@app.post("/users")
def add_user(name: str, db=Depends(get_db)):
    cursor =db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name, ))
    db.commit()
    return {"message": "User added successfully"}