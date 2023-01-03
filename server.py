from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', cupcakes = get_cupcakes('cupcakes.csv'))

@app.route('/cupcakes')
def all_cupcakes():
    return render_template('cupcakes.html', cupcakes = get_cupcakes('cupcakes.csv'))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake('cupcakes.csv', name)

    if cupcake:
        add_cupcake_dict('orders.csv', cupcake=cupcake)
        return redirect(url_for('order'))
    else:
        return 'Sorry cupcake not found.'


@app.route('/individual_cupcake/<name>')
def individual_cupcake(name):
    cupcake = find_cupcake('cupcakes.csv', name)
    
    if cupcake:
        return render_template('individual_cupcake.html', cupcake=cupcake)
    else:
        return 'Sorry cupcake not found.'

@app.route('/order')
def order():
    cupcakes = get_cupcakes('orders.csv')


    return render_template('order.html', cupcakes = cupcakes)



if __name__ == '__main__':
    app.debug = 'development'
    app.run(debug = True, port = 8000, host = 'localhost')
