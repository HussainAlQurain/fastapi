from muheetclubdb import Authors, Transaction, Accounts, Checks, ClubCategory, OfficeCategory, Expenses, OfficeClass

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from my_fastapi import GetFast

SQLALCHEMY_DATABASE_URL = "sqlite:///muheetclubdb.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()



### Get Methods:

#authors get
def get_authors():
    authors = []
    for row in session.query(Authors):
        authors.append({"id": row.id, "AuthorID": row.AuthorID, "LastName": row.LastName, "Nationality": row.Nationality})
    return authors

def get_one_author(id):
    authors = []
    for row in session.query(Authors).filter(Authors.id == id):
        authors.append({"id": row.id, "AuthorID": row.AuthorID, "LastName": row.LastName, "Nationality": row.Nationality})
    return authors

#transactions get
def get_transactions():
    transactions = []
    for row in session.query(Transaction):
        transactions.append({"id": row.id, "date": row.date, "transaction_description": row.transaction_description, "description": row.description, "description_extra": row.description_extra, "reference": row.reference, "Remarks": row.Remarks, "debit": row.debit, "credit": row.credit, "balance": row.balance, "checkno": row.checkno})
    return transactions

def get_one_transaction(id):
    transactions = []
    for row in session.query(Transaction).filter(Transaction.id == id):
        transactions.append({"id": row.id, "date": row.date, "transaction_description": row.transaction_description, "description": row.description, "description_extra": row.description_extra, "reference": row.reference, "Remarks": row.Remarks, "debit": row.debit, "credit": row.credit, "balance": row.balance, "checkno": row.checkno})
    return transactions

#Accounts get
def get_accounts():
    accounts = []
    for row in session.query(Accounts):
        accounts.append({"user_id": row.user_id, "username": row.username, "password": row.password, "email": row.email, "created_on": row.created_on, "last_login": row.last_login})
    return accounts

def get_one_account(user_id):
    accounts = []
    for row in session.query(Accounts).filter(Accounts.id == user_id):
        accounts.append({"user_id": row.user_id, "username": row.username, "password": row.password, "email": row.email, "created_on": row.created_on, "last_login": row.last_login})
    return accounts

#checks get

def get_checks():
    checks = []
    for row in session.query(Checks):
        checks.append({"id": row.id, "checkno": row.checkno, "amount": row.amount, "date": row.date, "issued_to": row.issued_to})
    return checks

def get_one_check(id):
    checks = []
    for row in session.query(Checks).filter(Checks.id == id):
        checks.append({"id": row.id, "checkno": row.checkno, "amount": row.amount, "date": row.date, "issued_to": row.issued_to})
    return checks


#club category get

def get_clubcategory():
    clubcategory = []
    for row in session.query(ClubCategory):
        clubcategory.append({"id": row.id, "category": row.category})
    return clubcategory

def get_one_clubcategory(id):
    clubcategory = []
    for row in session.query(ClubCategory).filter(ClubCategory.id == id):
        clubcategory.append({"id": row.id, "category": row.category})
    return clubcategory


#office category get

def get_officecategory():
    officecategory = []
    for row in session.query(OfficeCategory):
        officecategory.append({"id": row.id, "category": row.category})
    return officecategory

def get_one_officecategory(id):
    officecategory = []
    for row in session.query(OfficeCategory).filter(OfficeCategory.id == id):
        officecategory.append({"id": row.id, "category": row.category})
    return officecategory


#expenses get

def get_expenses():
    expenses = []
    for row in session.query(Expenses):
        expenses.append({"id": row.id, "amount": row.amount, "description": row.description, "office_category": row.office_category, "club_category": row.club_category, "from_checkno": row.from_checkno})
    return expenses

def get_one_expense(user_id):
    expenses = []
    for row in session.query(Expenses).filter(Expenses.id == user_id):
        expenses.append({"id": row.id, "amount": row.amount, "description": row.description, "office_category": row.office_category, "club_category": row.club_category, "from_checkno": row.from_checkno})
    return expenses


#office class get

def get_officeclass():
    officeclass = []
    for row in session.query(OfficeClass):
        officeclass.append({"id": row.id, "class_": row.class_})
    return officeclass

def get_one_officeclass(id):
    officeclass = []
    for row in session.query(OfficeClass).filter(OfficeClass.id == id):
        officeclass.append({"id": row.id, "class_": row.class_})
    return officeclass


### End of Get Methods


if __name__ == "__main__":
    pass