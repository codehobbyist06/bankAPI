from ariadne import QueryType
from .models import Banks, Branches

query = QueryType()

@query.field("getBranchesfromID")
def getBranchesfromID_resolver(obj,info,id):
    """
    This resolves queries for branches based in bank_id
    The number of required parameters can be set in the query
    """
    try:
        data = Banks.query.filter_by(id=id).first()
        branches = Branches.query.filter_by(bank_id=id)
        branches_data = []
        for branch in branches:
            branches_data.append(branch.to_dict())
        result = {
            'id' : data.id,
            'name': data.name,
            'branches': branches_data,
            'success':True,
        }
    except Exception:
        result = {
            'success':False,
            'errors': [f'No branch found for id: {id}'],
        }
    return result

@query.field("getBranchfromIFSC")
def getBranchfromIFSC_resolver(obj,info,ifsc):
    """
    This resolves queries for branch corresponding to given ifsc
    """
    try:
        branches = Branches.query.filter_by(ifsc=ifsc).first()
        result = branches.to_dict()
        result['success'] = True
    except Exception:
        result = {
            'success': False,
            'errors': [f'No branch found for ifsc: {ifsc}'],
        }
    return result

