from pydantic import BaseModel
from datetime import date as date2, datetime, time, timedelta


# Create ToDoRequest Base Model
class PAuthors(BaseModel):
   
   AuthorID: int
   LastName: str
   Nationality: str

class PTransaction(BaseModel):
   
   date: date2 = None
   transaction_description: str
   description: str
   description_extra: str
   reference: int #numeric
   Remarks: str
   debit: float
   credit: float
   balance: float
   checkno: int

   
class PAccounts(BaseModel):
   
   username: str
   password: str
   email: str
   created_on: date2 = None
   last_login: date2 = None
   
class PChecks(BaseModel):
   
   checkno: int
   amount: float
   date: date2 = None
   issued_to: str


class PClubCategory(BaseModel):
   
   category: str

class POfficeCategory(BaseModel):
   
   category: str

class PExpenses(BaseModel):
   
   amount: float
   description: str
   office_category: int
   club_category: int
   from_checkno: int


class POfficeClass(BaseModel):
   
   class_: str

if __name__ == "__main__":
    pass