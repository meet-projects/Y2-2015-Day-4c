from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from database_setup import Base, Person
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def view_my_friends():
    friends = []  # CHANGE THIS TO READ ALL FRIENDS FROM THE DATABASE
    return render_template('view_my_friends.html', friends=friends)


@app.route('/add', methods=['GET', 'POST'])
def add_friend():
    return render_template('add_friend.html')


if __name__ == '__main__':
    app.run(debug=True)
