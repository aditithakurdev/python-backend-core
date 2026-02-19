from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text

app = FastAPI()

@app.on_event("startup")
def test_db_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connected successfully 🚀")
    except Exception as e:
        print("Database connection failed ❌", e)

@app.get("/")
def root():
    return {"message": "Server is running 🚀"}
