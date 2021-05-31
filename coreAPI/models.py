from coreAPI import db
from sqlalchemy.dialects import postgresql

class Banks(db.Model):
    """
    Defines the Bank Model based on the provided 
    postgresql database
    """
    id = db.Column(postgresql.BIGINT,primary_key=True)
    name = db.Column(postgresql.VARCHAR(49))
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
        }

class Branches(db.Model):
    """
    Defines the Branch Model based on the provided 
    postgresql database
    """
    ifsc = db.Column(postgresql.VARCHAR(11),primary_key=True)
    bank_id = db.Column(postgresql.BIGINT)
    branch = db.Column(postgresql.VARCHAR(74))
    address = db.Column(postgresql.VARCHAR(195))
    city = db.Column(postgresql.VARCHAR(50))
    district = db.Column(postgresql.VARCHAR(50))
    state = db.Column(postgresql.VARCHAR(26))
    def to_dict(self):
        return {
            'ifsc':self.ifsc,
            'bank_id':self.bank_id,
            'branch':self.branch,
            'address':self.address,
            'city':self.city,
            'district':self.district,
            'state':self.state,
        }


# db.create_all()
