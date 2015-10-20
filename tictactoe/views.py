from flask import render_template

from tictactoe import app

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/game/<game_id>"):
    return render_template('game.html')
