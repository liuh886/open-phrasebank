# database.py
from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///database.db", echo=True)

def get_session():
    with Session(engine) as session:
        yield session

