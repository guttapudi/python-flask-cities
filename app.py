import os

from flask import Flask, jsonify

app = Flask(__name__)


cities = [
  {'city': 'Tokyo', 'population': 37435191},
  {'city': 'Delhi', 'population': 29399141},
  {'city': 'Shanghai', 'population': 26317104},
  {'city': 'Sao Paulo', 'population': 21846507},
  {'city': 'Mexico City', 'population': 21671908}
]

@app.route('/cities')
def get_cities():
  return jsonify(cities)

@app.route('/ping')
def ping():
  return "pong"

port = os.getenv('PORT', '8000')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))