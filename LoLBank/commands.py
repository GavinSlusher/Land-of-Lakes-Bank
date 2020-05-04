import click
from flask.cli import with_appcontext

from .extensions import db
from .models import addresses, clients, accounts
from .models import financial_advisors, clients_accounts, clients_advisors


# NOTE: Won't work until we finish creating database in models.py
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
