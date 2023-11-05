from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def HomeRoute():
  return {"message":"HomeRoute of User Management API"}

@app.get('/users')
def get_users():
  return {
    "username": "emily_white",
    "email": "emily.white@email.com",
    "full_name": "Emily White",
    "created_at": "2023-11-01 12:55:40"
  }