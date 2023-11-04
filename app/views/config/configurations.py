from app import *
from ...models.usuarios import Usuarios
from ...models.clientes import Clientes



@app.route("/configurations")
def configs():
    query = Usuarios.query.all()
    return render_template("conf/config.html", usuarios = query)


@app.route("/<int:id>/delete_usuario")
def delete_usuario(id):
    query = Usuarios.query.filter_by(id=id).first()
    db.session.delete(query)
    db.session.commit()
    return flash("removido com sucesso!")



@app.route("/<int:id>/delete_cliente")
def delete_cliente(id):
    query = Clientes.query.filter_by(id=id).first()
    db.session.delete(query)
    db.session.commit()
    return flash("removido com sucesso!")