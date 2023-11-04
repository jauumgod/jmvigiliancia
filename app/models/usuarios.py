from app import app, db, UserMixin


class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    permissao = db.Column(db.String(10), nullable=False)

    