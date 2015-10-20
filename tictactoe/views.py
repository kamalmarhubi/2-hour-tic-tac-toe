from flask import abort
from flask import render_template

import store

from tictactoe import app

# TODO: use app.config for this
game_store = store.PickledDictGameStore('/tmp/tictactoe')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/game/<game_id>")
def game(game_id):
    game = game_store.get(game_id)

    if game is None:
        abort(404)  # not found

    return render_template('game.html')
