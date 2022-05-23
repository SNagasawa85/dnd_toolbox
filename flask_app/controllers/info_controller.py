from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.user_model import User
from flask_app.models.character_model import Character
from flask_app.models.campaign_model import Campaign
import requests


@app.route('/api/show_info', methods=['POST'])
def show_info():
    session['api_req_index'] = request.form['index']
    print(session['api_req_index'])
    return redirect('/info')


@app.route('/api/show/info')
def api_get_info():
    string = session['api_req_index']
    discover = f'https://www.dnd5eapi.co/api/races/{string}'
    response = requests.get(url = discover)
    data = response.json()
    print(string)
    return jsonify(data)