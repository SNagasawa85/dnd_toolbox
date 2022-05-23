from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.character_model import Character
from flask_app.models.campaign_model import Campaign

@app.route('/view_campaigns')
def view_campaigns():
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'user_id' : session['user_id']}
    camps = Campaign.get_all_camps(data)
    print(camps)
    user_data = { 'id' : session['user_id']}
    user = User.get_one(user_data)
    return render_template('show_camp.html', camps = camps, user = user)

@app.route('/new_camp')
def new_campaign():
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'id' : session['user_id']}
    user = User.get_one(data)
    data = { 'user_id' : session['user_id']}
    chars = Character.get_all_chars(data)
    return render_template('new_camp.html',chars = chars,  user=user)


@app.route('/create_camp', methods=['POST'])
def create_campaign():
    if not Campaign.validate_camp(request.form):
        return redirect('/new_camp')
    print(request.form)
    Campaign.create_camp(request.form)
    return redirect('/view_campaigns')


@app.route('/edit/<int:id>')
def view_camp(id):
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'id': id}
    camp = Campaign.get_one_camp(data)
    udata = { 'id' : session['user_id']}
    user = User.get_one(udata)
    cdata = {'id' : camp.character_id}
    player = Character.get_one_char(cdata)
    char_data = { 'user_id':session['user_id']}
    chars = Character.get_all_chars(char_data)
    return render_template('edit_camp.html', user = user, player = player, camp = camp, chars = chars)


@app.route('/update_camp/<int:id>', methods=['POST'])
def update_camp(id):
    data = {
        'id' : id,
        'notes': request.form['notes']
    }
    Campaign.update_camp(data)
    return redirect(f'/edit/{id}')

@app.route('/delete/camp/<int:id>')
def delete_campaign(id):
    data = {
        'id' : id
    }
    Campaign.delete_camp(data)
    return redirect('/view_campaigns')


