# router.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from model import Phrase, get_phrases_by_discipline_and_section
from database import get_session

router = APIRouter()

class PhraseQuery(BaseModel):
    discipline: str
    section: str
    frequency_min: int
    num: int


# router.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from model import Phrase, get_phrases_by_discipline_and_section
from database import get_session

router = APIRouter()

class PhraseQuery(BaseModel):
    discipline: str
    section: str
    frequency_min: int
    num: int

@router.get("/phrases/")
async def read_phrases(query: PhraseQuery, session: Session = Depends(get_session)):
    phrases = get_phrases_by_discipline_and_section(query.discipline, query.section, query.frequency_min, query.num, session)
    if phrases:
        return phrases
    raise HTTPException(status_code=404, detail="No matching phrases found.")
