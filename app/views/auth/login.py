from app import app,render_template,login_user, LoginManager, timedelta, datetime, request, flash, redirect, url_for, check_password_hash
from ...models.usuarios import Usuarios
from ...controller.functions import create_user
from ...views.client.clientes import clientes

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

@app.route("/create_user", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        create_user(username, password)
        if create_user == True:
            flash('Usuario criado com sucesso!')
    
    else:
        flash('Não foi possivel criar o usuario!')
    
    return render_template("create_user.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # usuario = request.form['usuario']
        # senha = request.form['senha']

        # user = Usuarios.query.filter_by(username=usuario).first()

        # if not user or not check_password_hash(user.password, senha):
        #     flash("Usuario ou senha incorretos")
        #     return redirect(url_for("login"))
        
        # login_user(user, duration=datetime.timedelta(days=1))
        return redirect(url_for('clientes'))

    
    return render_template("auth/login.html")
