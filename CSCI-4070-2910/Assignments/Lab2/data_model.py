# data_model.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Base class for the class definitions
from sqlalchemy.orm import declarative_base  # Updated import to match SQLAlchemy 2.0 convention

Base = declarative_base()  # Corrected to use new 2.0 style declarative_base

# Classes
class Pokemon(Base):
    __tablename__ = 'Pokemon'  # Corrected from _tablename to __tablename__

    Id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    DexNumber = Column(Integer, nullable=False)
    Name = Column(String, nullable=True)
    Form = Column(String, nullable=True)
    Type1 = Column(String, nullable=True)
    Type2 = Column(String, nullable=True)
    Total = Column(Integer, nullable=True)
    HP = Column(Integer, nullable=True)
    Attack = Column(Integer, nullable=True)
    Defense = Column(Integer, nullable=True)
    SpecialAttack = Column(Integer, nullable=True)
    SpecialDefense = Column(Integer, nullable=True)
    Speed = Column(Integer, nullable=True)
    Generation = Column(Integer, nullable=True)

    def __repr__(self):  # Fixed method name from repr to __repr__
        return (f'{self.DexNumber}, {self.Name}, {self.Form}, {self.Type1}, '
                f'{self.Type2}, {self.Total}, {self.HP}, {self.Attack}, '
                f'{self.Defense}, {self.SpecialAttack}, {self.SpecialDefense}, '
                f'{self.Speed}, {self.Generation}')
