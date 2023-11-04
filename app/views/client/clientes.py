from app import app, render_template, flash, request, db, redirect, url_for
from ...models.clientes import Clientes


@app.route('/clientes', methods=['GET','POST'])
def clientes():
    if request.method == 'POST':
        c = Clientes()
        c.name_cliente = request.form['nome']
        c.email = request.form['email']
        c.endereco = request.form['endereco']
        c.bairro = request.form['bairro']
        c.cidade = request.form['cidade']
        c.mensalidade = request.form['mensalidade']
        c.ocorrencias = 0
        c.pagamento = 0
        db.session.add(c)
        db.session.commit()
        return redirect(url_for("todos_clientes"))
        
    return render_template('cadastro/clientes.html')


@app.route("/todos_clientes")
def todos_clientes():
    result = Clientes.query.all()
    return render_template("cadastro/todos_clientes.html", result = result)

