import uuid

from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from game import Game
import store

from tictactoe import app

# TODO: use app.config for this
game_store = store.PickledDictGameStore('/tmp/tictactoe')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/game", methods=['POST'])
def new_game():
    game_id = uuid.uuid4().hex
    game = Game()

    game_store.put(game_id, game)

    return redirect(url_for('game', game_id=game_id))


@app.route("/game/<game_id>")
def game(game_id):
    game = game_store.get(game_id)

    if game is None:
        abort(404)  # not found

    return render_template('game.html', game=game, game_id=game_id)


@app.route("/game/<game_id>/move", methods=['POST'])
def make_move(game_id):
    game = game_store.get(game_id)

    if game is None:
        abort(404)  # not found

    move = request.form.get('move', None)

    player, x, y = move.split('|')  # TODO: validate

    game.make_move(player.lower(), (int(x), int(y)))

    game_store.put(game_id, game)

    return redirect(url_for('game', game_id=game_id))
