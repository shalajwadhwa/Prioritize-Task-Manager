from flask.helpers import flash
from app import app
from app.models import db, User
from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

login = LoginManager(app)
app.secret_key = b'Enter Secret Key Here'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email, name, password = request.form.get('email'), request.form.get('name'), request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Address Already Exists')
            return redirect('/login')
        user = User(name=name, email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('auth/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/matrix')
    if request.method == 'POST':
        user = User.query.filter_by(email = request.form.get('email')).first()
        if user is None or not check_password_hash(user.password_hash, request.form.get('password')):
            flash('Invalid EMail or Password')
            return redirect('/login')
        login_user(user)
        return redirect('/matrix')
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')