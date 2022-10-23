from muheetclubdb import Authors, Transaction, Accounts, Checks, ClubCategory, OfficeCategory, Expenses, OfficeClass

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from my_fastapi import GetFast
from datetime import date as date2

today = date2.today()

SQLALCHEMY_DATABASE_URL = "sqlite:///muheetclubdb.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

### post methods
#example
#ed_user = Authors(AuthorID=4, LastName='Gurain', Nationality='Saudi')
#session.add(ed_user)
#session.commit()
###


def add_author(a_id=-1, ln='None', n='Saudi'):
    author = Authors(AuthorID=a_id, LastName=ln, Nationality=n)
    session.add(author)
    session.commit()
    

def add_transaction(d=today, td ="-", dsc='-', dsce = '-', ref=0, rm ='-', deb = -1.0, cred = -1.0, bal = -1.0, chk = -1):

    transaction = Transaction(date=d, transaction_description=td, description=dsc, description_extra=dsce, reference=ref, Remarks=rm, debit=deb, credit = cred, balance = bal, checkno = chk)
    session.add(transaction)
    session.commit()

def add_account(name='None', pas='None', em='None', created='None', login='None'):

    account = Accounts(username=name, password=pas, email=em, created_on=created, last_login=login)
    session.add(account)
    session.commit()

def add_check(chkno=-1, amt=-1, dt=today, issued='None'):

    check = Checks(checkno=chkno, amount=amt, date=dt, issued_to=issued)
    session.add(check)
    session.commit()


def add_clubcategory(ct='None'):

    clubcategory = ClubCategory(category = ct)
    session.add(clubcategory)
    session.commit()

def add_officecategory(ct='None'):

    officecategory = OfficeCategory(category = ct)
    session.add(officecategory)
    session.commit()

def add_expense(amt=-1, dsc ='None', octg =-1, cctg=-1, chkno=-1):

    expense = Expenses(amount=amt, description=dsc, office_category=octg, club_category=cctg, from_checkno=chkno)
    session.add(expense)
    session.commit()


def add_officeclass(cl='None'):

    officeclass = OfficeClass(class_ = cl)
    session.add(officeclass)
    session.commit()
###

if __name__ == "__main__":
    pass
