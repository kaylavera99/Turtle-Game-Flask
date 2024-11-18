from flask import Flask, render_template, jsonify, request
import turtle_game

app = Flask(__name__)

game = turtle_game.TurtleGame()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    direction = request.json.get('direction')
    if direction == "up":
        result = game.move_up()
    elif direction == "down":
        result = game.move_down()
    elif direction == "left":
        result = game.move_left()
    elif direction == "right":
        result = game.move_right()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)