from flask import Blueprint, render_template, request

from .extensions import db
from .forms import (ClientForm, AdvisorForm, AccountForm, UpdateClient,
                    DeleteForm, TablesForm)
# NOTE: Won't work until we finish models.py
from .models import clients, addresses
# from .models import addresses, clients, accounts
# from .models import financial_advisors, clients_accounts, clients_advisors


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/add_client', methods=['GET', 'POST'])
def add_client():

    form = ClientForm()

    if form.validate_on_submit():
        ssn = form.ssn.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        city = form.city.data
        state = form.state.data
        house_number = form.house_number.data
        zip_code = form.zip_code.data
        email = form.email.data

        new_address= addresses(
                               city=city,
                               state=state,
                               house_number=house_number,
                               #address_id=address_id,
                               zip_code=zip_code                               
        )

        new_client = clients(
                            ssn=ssn,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address_id=new_address
        )

        db.session.add(new_client)
        db.session.add(new_address)
        db.session.commit()

        print("Client added to the database")

    return render_template('add_client.html', form=form)


@main.route('/add_advisor', methods=['GET', 'POST'])
def add_advisor():

    form = AdvisorForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        area_of_expertise = form.expertise.data

    return render_template('add_advisor.html', form=form)

# at least one SELECT utilize a search/filter with a dynamically populated
# list of properties
@main.route('/search_database', methods=['GET', 'POST'])
def search_database():
    return render_template('search_database.html')

# add an account to an existing user
@main.route('/add_account', methods=['GET', 'POST'])
def add_account():
    form = AccountForm()
    if form.validate_on_submit():
        id = form.id.data
    # else:
        # return error message if invalid id entered

    return render_template('add_account.html', form=form)


@main.route('/update_client',  methods=['GET', 'POST'])
def update_client():
    form = UpdateClient()
    if form.validate_on_submit():
        id = form.id.data
        # return (return client data)
    # else:
        # return error message if invalid id entered

    return render_template('update_client.html', form=form)


@main.route('/delete_client', methods=['GET', 'POST'])
def delete_client():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data

    return render_template('delete_client.html', form=form)


@main.route('/view_tables', methods=['GET', 'POST'])
def view_tables():
    form = TablesForm()
    if form.validate_on_submit():

        table_wanted = form.tables.data
        print(table_wanted)

    if form.validate_on_submit():
        if table_wanted == "clients":
            print("User wants clients")            
            client_table = clients.query.all()
            for x in client_table:
                print(x.first_name)

            return render_template('client_table.html', form=form, client_table=client_table)
    
    if form.validate_on_submit():
        if table_wanted == "addresses":
            print("User wants addresses")            
            address_table = addresses.query.all()
            for x in address_table:
                print(x.state)
            
            return render_template('address_table.html', form=form, address_table=address_table)

        # clients = clients.form.data
        # addresses = form.addresses.data
        # accounts = form.accounts.data
        # financial_advisors = form.financial_advisors.data
        # clients_advisors = form.clients_advisors.data
        # clients_accounts = form.clients_accounts.data
    return render_template('view_tables.html', form=form)
