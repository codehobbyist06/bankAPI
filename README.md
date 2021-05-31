# BankAPI
This is an API built using python Flask framework to provide an interface
to the bank data provided by RBI (Reserve bank of India). It supports grapql 
queries at endpoint ("/gql").  

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
The application is currently deployed at

