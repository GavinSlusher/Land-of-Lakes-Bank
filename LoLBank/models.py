from .extensions import db


class addresses(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    house_number = db.Column(db.Integer())
    zip_code = db.Column(db.Integer())
    # client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)

# person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
class clients(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    # address_id = db.Column(db.Integer, db.ForeignKey('addresses.address_id'), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    # client_account_id(db.Integer, db.ForeignKey('clients_accounts.client_account_id'), nullable=False)
    # client_advisor_id(db.Integer, db.ForeignKey('client_advisors.client_advisor_id'), nullable=False)

class accounts(db.Model):
    account_id = db.Column(db.Integer, unique=True, primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    # client_account_id = db.Column(db.Integer, nullable=False, db.ForeignKey('accounts.account_id'))

# class financial_advisors(db.Model):
#     pass


# class clients_accounts(db.Model):
#     pass


# class clients_advisors(db.Model):
#     pass
