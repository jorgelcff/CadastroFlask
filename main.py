# Importar biblioteca Flask
from flask import Flask, render_template, request, redirect

# Inicializar aplicação
app = Flask(__name__)

# Lista de produtos
produtos = []

# Rota para página principal
@app.route('/')
def index():
    return redirect('/listar')

# Rota para página de listagem de produtos
@app.route('/listar')
def listar():
    # Ordenar produtos por valor do menor para o maior
    produtos_ordenados = sorted(produtos, key=lambda p: p['valor'])
    return render_template('listar.html', produtos=produtos_ordenados)

# Rota para página de cadastro de produtos
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Adicionar produto à lista
        produto = {
            'nome': request.form['nome'],
            'descricao': request.form['descricao'],
            'valor': float(request.form['valor']),
            'disponivel': request.form['disponivel'] == 'sim'
        }
        produtos.append(produto)
        return redirect('/listar')
    else:
        return render_template('cadastrar.html')

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
