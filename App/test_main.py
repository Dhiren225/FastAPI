from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

data={
  "ID": 2,
  "LAST_NAME": "Demo-1",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "Demo_1@gmai.com",
  "FIRST_NAME":"Demo-1",
  "CREATED_ON": "2022-06-27"
}

def test_read_customers():
    response = client.get("/getAllCustomers",json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_read_inexistent_customer():
    response = client.get("/getCustomerById/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Customer with id 10 not found"}

def test_update_inexistent_customer():
    response = client.get("/updateCustomer/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Customer with id 10 not found"}

def test_delete_inexistent_customer():
    response = client.get("/deleteCustomerById/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Customer with id 10 not found"}


def test_add_customer():
    response = client.post("/addCustomer",json={
  "ID": 1,
  "LAST_NAME": "string",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "string",
  "FIRST_NAME": "string",
  "CREATED_ON": "2022-06-28"
})
    assert response.status_code == 200
    assert response.json()=={
  "ID": 1,
  "LAST_NAME": "string",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "string",
  "FIRST_NAME": "string",
  "CREATED_ON": "2022-06-28"
}

def test_read_customer():
    response = client.get("/getCustomerById/1")
    assert response.status_code == 200
    assert response.json()=={
  "ID": 1,
  "LAST_NAME": "string",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "string",
  "FIRST_NAME":"string",
  "CREATED_ON": "2022-06-28"
}

def test_update_customer():
    response = client.put("/updateCustomer/1",json={
  "ID": 1,
  "LAST_NAME": "String",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "String",
  "FIRST_NAME": "String",
  "CREATED_ON": "2022-06-28"
})
    assert response.status_code == 200
    assert response.json()=={
  "ID": 1,
  "LAST_NAME": "String",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "String",
  "FIRST_NAME": "String",
  "CREATED_ON": "2022-06-28"
}

def test_delete_customer():
    response = client.delete("/deleteCustomerById/1")
    assert response.status_code == 200
    assert response.json()=={
  "ID": 1,
  "LAST_NAME": "String",
  "CUSTOMER_TYPE": "New",
  "EMAIL": "String",
  "FIRST_NAME": "String",
  "CREATED_ON": "2022-06-28"
}
