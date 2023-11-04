from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_manager, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import time
from datetime import datetime, timedelta
import psycopg2



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()
mi = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.init_app(app)




from .views.auth import login
from .views.config import configurations
from .views.client import clientes, relatorios
from .models import clientes, ocorrencias, pagamentos,usuarios
from .controller import auth, functions 