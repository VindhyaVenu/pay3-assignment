from fastapi import FastAPI, Header, HTTPException
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal

app = FastAPI()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

Base.metadata.create_all(bind=engine)

def check_auth(auth: str):
    if auth != "pay3-assignment":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/items")
def create_item(name: str, authorization: str = Header(None)):
    check_auth(authorization)
    db: Session = SessionLocal()
    item = Item(name=name)
    db.add(item)
    db.commit()
    return {"message": "Item created"}

@app.get("/items")
def get_items(authorization: str = Header(None)):
    check_auth(authorization)
    db: Session = SessionLocal()
    items = db.query(Item).all()
    return items