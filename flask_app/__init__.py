from flask import Flask
app=Flask(__name__)

app.secret_key="TotallySecretPassword"

DATABASE = 'dnd_toolbox_db'