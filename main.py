from fastapi import FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register_user(
  nome: str = Form(...),
  email: str = Form(...),
  senha: str = Form(...),
  db: Session = Depends(get_db)
):
  
  new_user = User(
    name = nome,
    email = email,
    password = senha
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return {
    "message": "User registered successfully",
    "user_id": new_user.id
  }
