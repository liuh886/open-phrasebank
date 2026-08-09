# model.py

# Part 1: quering the database
from sqlmodel import SQLModel, Field, Session, create_engine, select
from database import engine

class Phrase(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str
    frequency: int  # Adjusted from frequency_min for clarity in storing actual values
    discipline: str
    section: str

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_phrases_by_discipline_and_section(discipline: str, section: str, frequency_min: int, num: int, session: Session):
    statement = select(Phrase).where(
        Phrase.discipline == discipline,
        Phrase.section == section,
        Phrase.frequency >= frequency_min
    ).limit(num)
    results = session.exec(statement).all()
    return results


# Part 2: initializing the database

from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Ngram(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    text: str
    length: int
    categories: List["NgramCategory"] = Relationship(back_populates="ngram")

class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    discipline: str
    section: str
    ngrams: List["NgramCategory"] = Relationship(back_populates="category")

class NgramCategory(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ngram_id: int = Field(foreign_key="ngram.id")
    category_id: int = Field(foreign_key="category.id")
    frequency: int
    ngram: Ngram = Relationship(back_populates="categories")
    category: Category = Relationship(back_populates="ngrams")

class Sentence(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ngram_id: int = Field(foreign_key="ngram.id")
    category_id: int = Field(foreign_key="category.id")
    text: str
    bibliography: str
    ngram: Optional[Ngram] = Relationship(back_populates="sentences")
    category: Optional[Category] = Relationship(back_populates="sentences")
