from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    age: int
    gender: str
    course: str

@app.post("/register")
def register(student: Student):
    return {
        "message": "Registration Successful!",
        "student": student
    }