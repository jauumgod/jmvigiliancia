from app import app, db, datetime


class Pagamentos(db.Model):
    id_pag = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
