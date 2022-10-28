from flask import Flask, render_template, request
from flask_bootstrap import  Bootstrap5

from User import User

app = Flask(__name__)
bootstrap = Bootstrap5(app)

users = []


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/reg')
def reg():
    return render_template('registration.html')


@app.route('/auth', methods=['POST', 'GET'])
def auth():
    init_users()
    email = request.form['email']
    password = request.form['pass']
    for u in users:
        if u.email == email and u.password == password:
            return render_template('index.html')
    return render_template('login.html')


def init_users():
    user1 = User()
    user1.name = "Igor"
    user1.email = "email@email.ru"
    user1.password = "12345"
    users.append(user1)


if __name__ == '__main__':
    app.run()
