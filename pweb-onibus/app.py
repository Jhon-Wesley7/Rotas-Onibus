from flask import Flask, render_template, request, redirect

app = Flask(__name__)
routes = []

# Rota inicial - Listagem de rotas
@app.route('/')
def index():
    return render_template('index.html', routes=routes)

# Rota para adicionar uma nova rota
@app.route('/add', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        route = {
            'origin': request.form['origin'],
            'destination': request.form['destination'],
            'price': request.form['price']
        }
        routes.append(route)
        return redirect('/')
    return render_template('add_route.html')

# Rota para editar uma rota existente
@app.route('/edit/<int:route_id>', methods=['GET', 'POST'])
def edit_route(route_id):
    route = routes[route_id]
    if request.method == 'POST':
        route['origin'] = request.form['origin']
        route['destination'] = request.form['destination']
        route['price'] = request.form['price']
        return redirect('/')
    return render_template('edit_route.html', route=route, route_id=route_id)

# Rota para deletar uma rota existente
@app.route('/delete/<int:route_id>')
def delete_route(route_id):
    del routes[route_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)