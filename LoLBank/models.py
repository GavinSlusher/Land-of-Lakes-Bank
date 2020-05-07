from .extensions import db


class addresses(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    house_number = db.Column(db.Integer)
    zip_code = db.Column(db.Integer)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('clients.client_id'),
                          nullable=False)


class clients(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    address_id = db.Column(db.Integer,
                           db.ForeignKey('addresses.address_id'),
                           nullable=False)

    email = db.Column(db.String(255), nullable=False)
    client_account_id = db.Column(db.Integer,
                                  db.ForeignKey('clients_accounts.\
                                                 client_account_id'),
                                  nullable=False)

    client_advisor_id = db.Column(db.Integer,
                                  db.ForeignKey('client_advisors.\
                                                 client_advisor_id'),
                                  nullable=False)


class accounts(db.Model):
    account_id = db.Column(db.Integer, unique=True, primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    client_account_id = db.Column(db.Integer,
                                  db.ForeignKey('accounts.account_id'),
                                  nullable=False)


class financial_advisors(db.Model):
    advisor_id = db.Column(db.Integer, primary_key=True, nullable=False)
    # TO DO: DEFINE ENUM TYPES
    # area_of_expertise = db.Column(db.Enum(expertise), nullable=False)
    client_advisor_id = db.Column(db.Integer,
                                  db.ForeignKey('clients_advisors.\
                                                 client_advisor_id'),
                                  nullable=False)

    # String may need a size argument ie: String(size)
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)


class clients_accounts(db.Model):
    client_account_id = db.Column(db.Integer, unique=True, primary_key=True)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('clients.client_id'),
                          nullable=False)

    account_id = db.Column(db.Integer,
                           db.ForeignKey('accounts.account_id'),
                           nullable=False)


class clients_advisors(db.Model):
    client_advisor_id = db.Column(db.Integer, unique=True, primary_key=True)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('clients.client_id'),
                          nullable=False)

    advisor_id = db.Column(db.Integer,
                           db.ForeignKey('financial_advisors.advisor_id'),
                           nullable=False)
