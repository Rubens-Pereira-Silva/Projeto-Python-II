from flask import Flask, render_template, request, jsonify

import services.RelatorioService
from services import RelatorioService
from src.data.database import db

#Import das classes
from models.RelatorioDB import RelatorioDB

#Cria a aplicação flask
app = Flask(__name__)

#Configurações do App
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///relatorios.db"
db.init_app(app)
#Contexto do app
with app.app_context():
    db.create_all()

#Rotas

#POST relario
@app.route("/relatorio" ,methods=['POST'])
def relatorioPost():
    #Pega os dados recebidos
    dados = request.json
    return RelatorioService.RelatorioPOST(dados)


#GET Relatorios
@app.route("/relatorio" ,methods=['GET'])
def relatorioGet():
    relatorios = RelatorioDB.query.all()
    print(relatorios)

    return jsonify([
        {
            "id": relatorio.id,
            "temperatura": relatorio.temperatura,
            "umidade": relatorio.umidade,
            "pressao": relatorio.pressao,
            "luminosidade": relatorio.luminosidade,
            "qualidade_ar": relatorio.qualidade_ar
        }
        for relatorio in relatorios
    ])

#Rota Padrão
@app.route('/')
def home():
    return render_template('index.html')



#inicia a aplicação flask
app.run()