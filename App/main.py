from fastapi import FastAPI, HTTPException,Request,status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import model
import database
import datetime

# Initialize app
app = FastAPI()

# Create Customer Base Model
class Customer(BaseModel):
    ID:int
    FIRST_NAME:str
    LAST_NAME:str
    EMAIL:str
    CUSTOMER_TYPE:str
    CREATED_ON:datetime.date

# Get all customer records from the database
@app.get("/getAllCustomers")
def read_customers():
    # create a new database session
    session = Session(bind=database.engine,expire_on_commit=False)
    customer_list = session.query(model.Customers).all()
    # close the session
    session.close()
    return customer_list

# Get Customer records from the database by ID
@app.get("/getCustomerById/{id}")
def read_customer(id: int):
    # create a new database session
    session = Session(bind=database.engine,expire_on_commit=False)
    customer = session.query(model.Customers).get(id)
    #check if customer with given id exists. If not, raise exception
    if customer:
        # close the session
        session.close()
        return customer
    else:
        raise HTTPException(status_code=404, detail=f"Customer with id {id} not found")
    
# Insert a new record in the database
@app.post("/addCustomer")
def add_customer(customer: Customer):
    # create a new database session
    session = Session(bind=database.engine,expire_on_commit=False)

    customer_found=session.query(model.Customers).get(customer.ID)
    #check if customer with given id already exists.
    if customer_found:
        raise HTTPException(status_code=409, detail=f"Customer with id {customer.ID} already exists")
    else:
        new_customer=model.Customers(
        ID=customer.ID,
        FIRST_NAME=customer.FIRST_NAME,
        LAST_NAME=customer.LAST_NAME,
        EMAIL=customer.EMAIL,
        CUSTOMER_TYPE=customer.CUSTOMER_TYPE,
        CREATED_ON=customer.CREATED_ON
        )
        # add it to the session and commit
        session.add(new_customer)
        session.commit()
        # close the session
        session.close()
    return new_customer
        
    
# Updating record in the database
@app.put("/updateCustomer/{customerId}")
def update_customer(customerId:int,customer: Customer):
    # create a new database session
    session = Session(bind=database.engine,expire_on_commit=False)
    update_customer=session.query(model.Customers).filter(model.Customers.ID==customerId).first()
    #check if customer with given id exists. If not, raise exception
    if update_customer:
        update_customer.FIRST_NAME=customer.FIRST_NAME
        update_customer.LAST_NAME=customer.LAST_NAME
        update_customer.EMAIL=customer.EMAIL
        update_customer.CUSTOMER_TYPE=customer.CUSTOMER_TYPE
        update_customer.CREATED_ON=customer.CREATED_ON
        session.commit()
        # close the session
        session.close()
        return update_customer
    else:
        raise HTTPException(status_code=404, detail=f"Customer with id {customerId} not found")
    
# Delete record in the database
@app.delete("/deleteCustomerById/{id}")
def delete_customer(id: int):
    # create a new database session
    session = Session(bind=database.engine,expire_on_commit=False)
    customer= session.query(model.Customers).get(id)
    #check if customer with given id exists. If not, raise exception
    if customer:
        # delete it from the session and commit it
        session.delete(customer)
        session.commit()
        # close the session
        session.close()
        return customer
    else:
        raise HTTPException(status_code=404, detail=f"Customer with id {id} not found")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

