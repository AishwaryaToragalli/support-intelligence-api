from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import get_db
from models import TicketModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Support Intelligence API", version="1.0.0")


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str = "medium"


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str

    class Config:
        from_attributes = True


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/tickets", response_model=TicketResponse, status_code=201)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = TicketModel(
        title=ticket.title, description=ticket.description, priority=ticket.priority
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


@app.get("/tickets", response_model=list[TicketResponse])
def get_tickets(db: Session = Depends(get_db)):
    return db.query(TicketModel).all()


@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(TicketModel).filter(TicketModel.id == ticket_id).first()

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return ticket


@app.get("/")
def read_root():
    return {"status": "FastAPI is working successfully"}
