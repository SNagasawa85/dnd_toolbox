from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.campaign_model import Campaign
from flask_app.models.character_model import Character


@app.route('/view_characters')
def view_characters():
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'user_id': session['user_id']}
    characters = Character.get_all_chars(data)
    data = { 'id' : session['user_id'] }
    user = User.get_one(data)
    return render_template('show_char.html', characters=characters, user = user)

@app.route('/new_char')
def new_char():
    if 'user_id' not in session:
        return redirect('/welcome')
    if 'create' not in session:
        user_id = session ['user_id']
        session.clear()
        session['user_id'] = user_id
    data = { 'id': session['user_id']}
    user = User.get_one(data)
    allchars = Character.show_all_chars()
    return render_template('new_char.html', allchars = allchars, user=user)

@app.route('/create_char', methods=['POST'])
def create_char():
    print(request.form)
    if not Character.validate_input(request.form):
        session['name'] = request.form['name']
        session['char_class'] = request.form['char_class']
        session['race'] = request.form['race']
        session['strength'] = request.form['strength']
        session['constitution'] = request.form['constitution']
        session['dexterity'] = request.form['dexterity']
        session['intelligence'] = request.form['intelligence']
        session['wisdom'] = request.form['wisdom']
        session['charisma'] = request.form['charisma']
        session['notes'] = request.form['notes']
        session['create'] = 'create'
        return redirect('/new_char')
    Character.create_char(request.form)
    user_id = session ['user_id']
    session.clear()
    session['user_id'] = user_id
    return redirect('/view_characters')

@app.route('/reuse_char/<int:id>', methods=['POST'])
def reuse_char(id):
    print(request.form)
    if not Character.validate_input(request.form):
        session['name'] = request.form['name']
        session['char_class'] = request.form['char_class']
        session['race'] = request.form['race']
        session['strength'] = request.form['strength']
        session['constitution'] = request.form['constitution']
        session['dexterity'] = request.form['dexterity']
        session['intelligence'] = request.form['intelligence']
        session['wisdom'] = request.form['wisdom']
        session['charisma'] = request.form['charisma']
        session['notes'] = request.form['notes']
        session['reuse'] = 'reuse'
        return redirect(f'/reuse/{id}')
    Character.create_char(request.form)
    user_id = session ['user_id']
    session.clear()
    session['user_id'] = user_id
    return redirect('/view_characters')

@app.route('/edit/character/<int:id>')
def edit_char(id):
    if 'user_id' not in session:
        return redirect('/welcome')
    data = { 'id': session['user_id']}
    user = User.get_one(data)
    cdata = { 'id': id}
    char = Character.get_one_char(cdata)
    return render_template('edit_char.html',char = char, user = user)

@app.route('/delete/character/<int:id>')
def delete_char(id):
    data = {'id': id }
    Character.delete_char(data)
    return redirect('/view_characters')

@app.route('/change_player/<int:id>', methods=['POST'])
def change_player(id):
    data = {
        'id' : id,
        'character_id': request.form['character_id']
    }
    Campaign.change_character(data)
    return redirect('/view_campaigns')

@app.route('/update_char/<int:id>', methods=['POST'])
def update_char(id):
    data = {
        'id': id,
        'notes': request.form['notes']
    }
    Character.update_char_notes(data)
    return redirect(f'/edit/character/{id}')

@app.route('/reuse/<int:id>')
def resuse(id):
    if 'user_id' not in session:
        return redirect('/')
    if 'reuse' not in session:
        user_id = session ['user_id']
        session.clear()
        session['user_id'] = user_id
    rechar = Character.get_one_char({ 'id' : id })
    session['notes'] = rechar.notes
    user = User.get_one({ 'id': session['user_id']})
    return render_template('/reuse.html',user = user, rechar = rechar)
    





