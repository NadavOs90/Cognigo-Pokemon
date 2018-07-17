from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal
from pokemon import new_pokemon, search
from wtforms import Form, StringField, TextAreaField, validators


app = Flask(__name__)
app.debug = True
api = Api(app)
cache = {}


# class Search(Resource):
#     prefix_str = StringField('', [validators.Length(min=1)])
#
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#
#
#
# class NewPokemon(Form):
#     pokemon_json_string = TextAreaField('Enter Pokemon JSON')
#
#
#
# @app.route('/')
# def hello():
#     return render_template('pokemon_home.html')
#
#
# @app.route('/add_pokemon', methods=['GET', 'POST'])
# def add_pokemon():
#     global cache
#     form = NewPokemon(request.form)
#     if request.method == 'POST' and form.validate():
#         pokemon_obj = form.pokemon_json_string.data
#         res = new_pokemon(pokemon_obj)
#         if res:
#             cache = {}
#             return render_template('success.html')
#         return render_template('add_pokemon.html', form=form)
#     return render_template('add_pokemon.html', form=form)
#
#
# @app.route('/search_prefix', methods=['GET', 'POST'])
# def search_prefix():
#     form = Search(request.form)
#     if request.method == 'POST' and form.validate():
#         prefix = form.prefix_str.data
#         if cache.get(prefix):
#             res = cache[prefix]
#         else:
#             res = search(prefix)
#             cache[prefix] = res
#         return render_template('search_prefix.html', form=form, pokemons=res)
#     return render_template('search_prefix.html', form=form)

# class Pokemon(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('name', type=str, location='json', required=True)


@app.route('/Create a new Pokemon/<string:pokemon_json>')
def add_pokemon(pokemon_json):
    # new_pokemon(pokemon_json)
    return pokemon_json

@app.route('/Auto-complete/<string:prefix>')
def search_prefix(prefix):
    res = search(prefix)
    return jsonify({'Pokemons': res})


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
