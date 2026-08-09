# initial file for api module

from sqlmodel import Session, create_engine
from models import SQLModel, Ngram, Category, NgramCategory, Sentence

# Database engine
engine = create_engine("sqlite:///database.db")

def create_tables():
    SQLModel.metadata.create_all(engine)

def insert_initial_data():
    with Session(engine) as session:
        # Example data insertion
        ngram1 = Ngram(text="the study", length=2)
        category1 = Category(discipline="Physics", section="Abstract")
        session.add(ngram1)
        session.add(category1)

        ngram_category1 = NgramCategory(ngram_id=1, category_id=1, frequency=5)
        session.add(ngram_category1)

        # Commit the session to save all changes
        session.commit()

if __name__ == "__main__":
    create_tables()
    insert_initial_data()
