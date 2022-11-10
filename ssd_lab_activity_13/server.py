from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, UserMixin, login_user, logout_user, login_required, login_manager)
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretKey'

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/user/signin', methods=['POST'])
def do_signin():
    if(request.method == 'POST'):
        req = request.get_json()
        email = req['email']
        pwd = req['password']

    check_user = User.query.filter_by(email=email).first()
    if(check_user):
        if(check_user.password == pwd):
            login_user(check_user)
            return "Logged in successfully", 400
        else:
            return "Incorrect Password", 500


@app.route('/user/signout', methods=['GET'])
@login_required
def do_singout():
    logout_user()
    return "Logged out successfully", 400


@app.route('/user/signup', methods=['POST'])
def do_signup():
    if(request.method == 'POST'):
        req = request.get_json()
        username = req['name']
        em = req['email']
        pwd = req['password']
    newUser = User(email=em, name=username, password=pwd)

    db.session.add(newUser)
    db.session.commit()
    return "Account created succesfully"


with app.app_context():
    db.create_all()


def signin():
    email = input("Enter Email")
    pwd = input("Enter Password")
    payload = {
        "email": email,
        "password": pwd
    }

    resp = requests.post("127.0.0.1:5000/user/signin", json=payload).content.decode()

    print(resp)

def signout():
    # email = input("Enter Email")
    # pwd = input("Enter Password")
    # payload = {
    #     "email": email,
    #     "password": pwd
    # }

    resp = requests.get("127.0.0.1:5000/user/signout").content.decode()

    print(resp)

if "__main__" == __name__:
    app.run(host="127.0.0.1", port="5000", debug=True)