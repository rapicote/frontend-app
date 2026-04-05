import os
import sys

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('user.html', users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)