from flask import Flask, render_template, request, jsonify
from src.data.database import db

#Import das classes
from models.RelatorioDB import RelatorioDB

#Cria a aplicação flask
app = Flask(__name__)

#Banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///relatorios.db"

with app.app_context():
    db.init_app(app)
    db.create_all()

#Rotas

#POST relario
@app.route("/relatorio" ,methods=['POST'])
def relatorioPost():
    #Pega os dados recebidos
    dados = request.json

    #Tranforma os dados recebidos em uma instacia do relatorio
    relatorio = RelatorioDB(
        temperatura=dados['temperatura'],
        umidade=dados['umidade'],
        pressao=dados['pressao'],
        luminosidade=dados['luminosidade'],
        qualidade_ar=dados['qualidade_ar']
    )

    #adiciona o relatorio no banco de dados
    db.session.add(relatorio)
    db.session.commit()

    #retorna a mensagem de sucesso
    return {"mensagem" : "Relatorio Recebido"}, 200

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