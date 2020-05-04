from flask import Blueprint, render_template

from .extensions import db
# NOTE: Won't work until we finish models.py
# from .models import addresses, clients, accounts
# from .models import financial_advisors, clients_accounts, clients_advisors


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')
