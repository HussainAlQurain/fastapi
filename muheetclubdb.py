from sqlalchemy import Column, Integer, String, Date, Numeric, Float
from sqlalchemy import create_engine

engine = create_engine('sqlite:///muheetclubdb.db', echo = True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Authors(Base):
   __tablename__ = 'Authors'
   
   id = Column(Integer, primary_key=True)
   AuthorID = Column(Integer)
   LastName = Column(String)
   Nationality = Column(String)

class Transaction(Base):
   __tablename__ = 'Transaction'
   
   id = Column(Integer, primary_key=True)
   date = Column(Date)
   transaction_description = Column(String)
   description = Column(String)
   description_extra = Column(String)
   reference = Column(Numeric)
   Remarks = Column(String)
   debit = Column(Float)
   credit = Column(Float)
   balance = Column(Float)
   checkno = Column(Integer)

   
class Accounts(Base):
   __tablename__ = 'Accounts'
   
   user_id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)
   email = Column(String)
   created_on = Column(Date)
   last_login = Column(Date)
   
class Checks(Base):
   __tablename__ = 'Checks'
   
   id = Column(Integer, primary_key=True)
   checkno = Column(Integer)
   amount = Column(Float)
   date = Column(Date)
   issued_to = Column(String)


class ClubCategory(Base):
   __tablename__ = 'ClubCategory'
   
   id = Column(Integer, primary_key=True)
   category = Column(String)

class OfficeCategory(Base):
   __tablename__ = 'OfficeCategory'
   
   id = Column(Integer, primary_key=True)
   category = Column(String)

class Expenses(Base):
   __tablename__ = 'Expenses'
   
   id = Column(Integer, primary_key=True)
   amount = Column(Float)
   description = Column(String)
   office_category = Column(Integer)
   club_category = Column(Integer)
   from_checkno = Column(Integer)


class OfficeClass(Base):
   __tablename__ = 'OfficeClass'
   
   id = Column(Integer, primary_key=True)
   class_ = Column(String)

if __name__ == "__main__":
   Base.metadata.create_all(engine)