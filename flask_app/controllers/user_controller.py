from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.character_model import Character
from flask_app.models.campaign_model import Campaign

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
# first visit/root page
def root():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/welcome')

@app.route('/welcome')
# first page if user not logged in
def welcome():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('landing.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_all_present(request.form):
        return redirect('/welcome')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'pw_hash' : pw_hash,
    }
    user_id = User.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = { 'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid email or password!', 'err.login')
        return redirect('/welcome')
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form['pw']):
        flash('Invalid email or password!', 'err.login')
        return redirect('/welcome')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'id':session['user_id']}
    user=User.get_one(data)
    data = { 'user_id' : session['user_id']}
    char = Character.most_recent_char(data)
    camp = Campaign.most_recent_camp(data)
    return render_template('dashboard.html',camp=camp, user=user, char=char)

@app.route('/dice_roll')
def dice_roller():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_one({'id' : session['user_id']})
    return render_template('dice_roller.html', user=user)

@app.route('/info')
def info():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_one({ 'id':session['user_id']})
    return render_template('test.html', user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/welcome')