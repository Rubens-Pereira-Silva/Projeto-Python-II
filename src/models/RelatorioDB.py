from datetime import date, datetime

from src.data.database import db

class RelatorioDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float)
    umidade = db.Column(db.Float)
    pressao = db.Column(db.Float)
    luminosidade = db.Column(db.Float)
    qualidade_ar = db.Column(db.Float)
    data = db.Column(db.DateTime, default=datetime.now)
