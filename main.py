from fastapi import FastAPI
from my_fastapi import GetFast, PostFast, schemas


app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Home Page"}

@app.get("/authors")
async def authors():
    return GetFast.get_authors()


@app.get("/transactions")
async def transactions():
    return GetFast.get_transactions()

@app.get("/accounts")
async def accounts():
    return GetFast.get_accounts()

@app.get("/checks")
async def checks():
    return GetFast.get_checks()

@app.get("/clubcategory")
async def clubcategory():
    return GetFast.get_clubcategory()

@app.get("/officecategory")
async def officecategory():
    return GetFast.get_officecategory()

@app.get("/expenses")
async def expenses():
    return GetFast.get_expenses()

@app.get("/officeclass")
async def officeclass():
    return GetFast.get_officeclass()

##start of post methods
@app.post("/author/")
async def create_author(auth : schemas.PAuthors):
    PostFast.add_author(auth.AuthorID, auth.LastName, auth.Nationality)
    return f'Created Author with {auth}'


@app.post("/transaction/")
async def create_transaction(tran : schemas.PTransaction):
    PostFast.add_transaction(tran.date, tran.transaction_description, tran.description, tran.description_extra, tran.reference, tran.Remarks, tran.debit, tran.credit, tran.balance, tran.checkno)
    return f'Created transaction with {tran}'


@app.post("/account/")
async def create_account(acc : schemas.PAccounts):
    PostFast.add_account(acc.username, acc.password, acc.email, acc.created_on, acc.last_login)
    return f'Created Account with {acc}'


@app.post("/check/")
async def create_check(chk : schemas.PChecks):
    PostFast.add_check(chk.checkno, chk.amount, chk.date, chk.issued_to)
    return f'Created check with {chk}'


@app.post("/clubcategory/")
async def create_clubcategory(clctg : schemas.PClubCategory):
    PostFast.add_clubcategory(clctg.category)
    return f'Created ClubCategory with {clctg}'

@app.post("/officecategory/")
async def create_officecategory(ofctg : schemas.POfficeCategory):
    PostFast.add_officecategory(ofctg.category)
    return f'Created OfficeCategory with {ofctg}'

@app.post("/expense/")
async def create_expense(exp : schemas.PExpenses):
    PostFast.add_expense(exp.amount, exp.description,exp.office_category,exp.club_category,exp.from_checkno)
    return f'Created expense with {exp}'


@app.post("/officeclass/")
async def create_officeclass(offcls : schemas.POfficeClass):
    PostFast.add_officeclass(offcls.class_)
    return f'Created OfficeClass with {offcls}'


