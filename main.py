from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from passlib.context import CryptContext


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello Space!"}


DATABASE_URL = "sqlite:///./test/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


Base.metadata.ceate_all(bind=engine)


class UserCreate(BaseModel):
    username: str
    password: str


@app.post("/register")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)

    db_user = User(username=user.username, paswword=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User registered successfully!"}


def get_password_hash(password: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)