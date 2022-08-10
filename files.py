import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

base= declarative_base()

class FILE(base):
    __tablename__ ="File"
    id=Column(Integer, primary_key=True)
    file_name=Column(String,nullable=False)

if __name__ == "__main__":
    engine = create_engine('sqlite:///file_db.sqlite3')
    base.metadata.create_all(engine)