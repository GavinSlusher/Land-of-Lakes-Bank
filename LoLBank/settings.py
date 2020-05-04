import os

# When use flask run, get the settings from the .env folder and get the URI
# Note: the .env file should not be in the Development branch b/c Heroku.
# On Heroku, the environment variables need to be manually entered


# Get the things that are in the environment
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False
