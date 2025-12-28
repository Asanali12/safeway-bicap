from flask import Flask
import math

app = Flask(__name__)

@app.route('/coord/<x1>/<y1>/<x2>/<y2>')
def func(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return f"Расстояние между точками: {distance}"

if __name__ == '__main__':
    app.run(debug=True)
