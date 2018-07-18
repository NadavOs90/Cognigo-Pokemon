from flask import Flask, request, jsonify
from flask_restful import Api
from pokemon import new_pokemon, search


app = Flask(__name__)
app.debug = True
api = Api(app)
cache = {}


@app.route('/Create a new Pokemon', methods=['Put'])
def add_pokemon():
    pokemon_json = request.get_json()
    new_pokemon(pokemon_json)
    return jsonify({'Created': pokemon_json['name']})


@app.route('/Auto-complete/<string:prefix>')
def search_prefix(prefix):
    res = search(prefix)
    return jsonify({'Pokemons': res})


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
