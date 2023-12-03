from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    Name = Column(String, index=True)
    Age = Column(Integer)

    def __rep__(self):
        return '<User %r>' % (self.id)
    
    