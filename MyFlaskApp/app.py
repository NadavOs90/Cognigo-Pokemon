from flask import Flask, render_template, request, redirect
from pokemon import new_pokemon, search
from wtforms import Form, StringField, TextAreaField, validators


app = Flask(__name__)
app.debug = True

cache = {}


class Search(Form):
    prefix_str = StringField('', [validators.Length(min=1)])


class NewPokemon(Form):
    pokemon_json_string = TextAreaField('Enter Pokemon JSON')


@app.route('/')
def hello():
    return render_template('pokemon_home.html')


@app.route('/add_pokemon', methods=['GET', 'POST'])
def add_pokemon():
    global cache
    form = NewPokemon(request.form)
    if request.method == 'POST' and form.validate():
        pokemon_obj = form.pokemon_json_string.data
        res = new_pokemon(pokemon_obj)
        if res:
            cache = {}
            return render_template('success.html')
        return render_template('add_pokemon.html', form=form)
    return render_template('add_pokemon.html', form=form)


@app.route('/search_prefix', methods=['GET', 'POST'])
def search_prefix():
    form = Search(request.form)
    if request.method == 'POST' and form.validate():
        prefix = form.prefix_str.data
        if cache.get(prefix):
            res = cache[prefix]
        else:
            res = search(prefix)
            cache[prefix] = res
        return render_template('search_prefix.html', form=form, pokemons=res)
    return render_template('search_prefix.html', form=form)


if __name__ == '__main__':
    app.run()
