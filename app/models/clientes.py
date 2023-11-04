from app import app, db, datetime


class Clientes(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    name_cliente= db.Column(db.String(255))
    endereco = db.Column(db.String(150), nullable=False)
    bairro = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    email = db.Column(db.String(150))
    mensalidade = db.Column(db.Float())
    
    ocorrencias = db.Column(db.Integer, db.ForeignKey('ocorrencias.id_ocr'))
    pagamento = db.Column(db.Integer, db.ForeignKey('pagamentos.id_pag'))