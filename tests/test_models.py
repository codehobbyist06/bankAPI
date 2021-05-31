import pytest
from coreAPI.models import Banks, Branches

def test_bank_model():
  """
  Generates mock bank objects to test the model
  """
  mock_bank_data = Banks(id=1,name='State Bank of India')
  result = {
    'id':1,
    'name':'State Bank of India',
  }
  assert mock_bank_data.to_dict() == result

def test_branch_model():
  """
  Generates mock branch objects to test the model
  """
  mock_branch_data = Branches(ifsc='SBI000234455',bank_id=26,branch='Mock_Branch', 
                              address='Mock_address',city='Mock_city',district='Mock District', 
                              state='Mock State')
  result = {
        'ifsc': 'SBI000234455',
        'bank_id':26,
        'branch':'Mock_Branch',
        'address':'Mock_address',
        'city':'Mock_city',
        'district':'Mock District',
        'state':'Mock State',
  }
  assert mock_branch_data.to_dict() == result