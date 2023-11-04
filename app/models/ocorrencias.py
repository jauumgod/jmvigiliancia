from app import app, db, datetime


class Ocorrencias(db.Model):
    id_ocr = db.Column(db.Integer, primary_key=True)
    nome_ocorrencia = db.Column(db.String(150))
    nivel = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())