from fastapi import FastAPI

app = FastAPI(title="Task Management API")


@app.get("/")
def home():
    return {"message": "Task Management API is running"}