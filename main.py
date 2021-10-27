from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(width=15, height=15)
    return render_template('index.html')

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html',
                            universe = game.world,
                            counter=game.counter,
                            old_universe = game.old_world)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
