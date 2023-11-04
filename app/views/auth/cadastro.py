import time
from app import app, request, url_for, redirect, render_template, flash, db,generate_password_hash
from ...models.usuarios import Usuarios



@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = Usuarios()
        user.username = request.form['username']
        user.password = generate_password_hash(request.form['password'])
        user.permissao = "None"
         
        query = Usuarios.query.filter_by(username=user.username).first()

        if query:
            flash("Usuario Já existe")
            time.sleep(2)
            return redirect("configs")

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("configs"))

    return render_template("auth/cadastro.html")


    