# BankAPI
This is an API built using python Flask framework to provide an interface
to the bank data provided by RBI (Reserve bank of India). It supports grapql 
queries at endpoint ("/gql").  

The API uses ariadne, a schema-first approach based python-graphql library which allows us
to define custom schema for our queries using SDL(Schema Definition Language).

The bank data is saved in a postgres database. The database has been interfaced with python
using the python-sqlalchemy library.

# Workflow
* The queries made to "/gql" endpoint are resolved by query resolvers in queries.py
and the required data is provided to the route resolvers. The route resolvers then
extract the information depending on the attributes requested and send it bank to 
the client.
* In case of any sever side errors, the application responds with appropriate
log information.

# Installation
* To install via git
  ```
    venv myenv ---> Create a virtual environment
    cd myenv
    source bin/activate  ---> Activate the virtual environment(For Linux)
    .\env\Scripts\activate  ---> Activate the virtual environment(For Windows)
    
    git clone https://github.com/codehobbyist06/bankAPI.git
    cd bankAPI
    pip install -r requirements.txt
    python run.py ---> Runs the app locally at localhost
  ```

* To run tests
  ```
    pip install -r test-requirements.txt
    python -m pytest
  ```
Following is the schema for supported queries:
```
type Query {
    getBranchesfromID(id: ID!): Banks
    getBranchfromIFSC(ifsc: ID!): Branches
}
```
e.g:
```
query = """ query getBranchesfromID {
  getBranchesfromID(id: "600") {
    name
    branches {
        ifsc
        branch
        address
      city
      district
      state
    }
    errors
  }
} """
```
```
query = """ query getBranchfromIFSC {
  getBranchfromIFSC(ifsc: "1") {
    branch
    address
    errors
  }
} """
```
The application is currently deployed at https://bankapp06.herokuapp.com/gql

