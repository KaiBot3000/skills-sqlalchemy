from model import *

def get_8():
	print Brand.query.get(8)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # (Model.name, Model.brand_name, Model.headquarters)

    # cars = db.session.query.filter(year=year).all()
    # for Model.name, Model.brand_name, Model.headquarters in cars:
    # 	print "Model: %s, Brand: %s, HQ: %s" % (name, brand_name, hq)

    cars = db.session.query(Model).filter_by(year=year).all()



#########################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."