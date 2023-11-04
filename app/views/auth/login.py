
from app import *
from ...models.usuarios import Usuarios
from ...views.client.clientes import clientes
import datetime

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        user = Usuarios.query.filter_by(username=usuario).first()

        if not user or not check_password_hash(user.password, senha):
            flash("Usuario ou senha incorretos")
            return redirect(url_for("login"))
        
        login_user(user, duration=datetime.timedelta(days=1))
        time.sleep(1)
        return redirect(url_for('homepage'))

    
    return render_template("auth/login.html")


@login_required
@app.route("/logout")
def logout():
    logout_user()
    time.sleep(1)
    return redirect(url_for("login"))