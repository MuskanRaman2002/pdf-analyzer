import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Float,DateTime
from datetime import  datetime
from sqlalchemy.ext.declarative import declarative_base

base= declarative_base()

class UserInput(base):
    __tablename__ ='userinputs'

    id=Column(Integer, primary_key=True)
    name=Column(String,nullable=False)
    size=Column(Integer,nullable=False)
    location=Column(String,nullable=False)
    create_at=Column(DateTime,default=datetime.utcnow,nullable=False)

    def __repr__(self) -> str:
        return f'{self.id}   {self.name}     {self.location}    {self.create_at}    {self.size}'

if __name__ == "__main__":
    engine=create_engine('sqlite:///file_db.sqlite3')
    base.metadata.create_all(engine)