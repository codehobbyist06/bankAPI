import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/"

query1 = """ query getBranchesfromID {
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
query2 = """ query getBranchfromIFSC {
  getBranchfromIFSC(ifsc: "1") {
    branch
    address
    errors
  }
} """
query3 = """ query getBranchesfromID {
  getBranchesfromID(id: "1") {
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

query4 = """ query getBranchfromIFSC {
  getBranchfromIFSC(ifsc: "SBIN0015250") {
    branch
    address
    errors
  }
} """

def test_post():
  """
  Tests the API for multiple post and get requests
  """
  response = requests.get(BASE_URL+'/gql')
  assert response.status_code == 200

  response = requests.post(BASE_URL+'/gql',json={'query':query1})
  assert response.json()['data']['getBranchesfromID']['errors'] == ['No branch found for id: 600']

  response = requests.post(BASE_URL+'/gql',json={'query':query2})
  assert response.json()['data']['getBranchfromIFSC']['errors'] == ['No branch found for ifsc: 1']

  response = requests.post(BASE_URL+'/gql',json={'query':query3})
  assert response.status_code == 200

  response = requests.post(BASE_URL+'/gql',json={'query':query4})
  assert response.status_code == 200
    

