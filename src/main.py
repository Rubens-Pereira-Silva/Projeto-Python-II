from flask import Flask, render_template, request, jsonify

from src.models.RelatorioRecebido import RelatorioRecebido

#Cria a aplicação flask
app = Flask(__name__)

#Variaveis
lista_relatorios = []

#Rotas

#POST relario
@app.route("/relatorio" ,methods=['POST'])
def relatorioPost():
    #Pega os dados recebidos
    dados = request.json

    #Tranforma os dados recebidos em uma instacia do relatorio
    relatorio = RelatorioRecebido(
        dados['temperatura'],
        dados['umidade'],
        dados['pressao'],
        dados['luminosidade'],
        dados['qualidade_ar']
    )
    #adicioa o relatorio na lista de relatorios
    lista_relatorios.append(relatorio)

    #retorna a mensagem de sucesso
    return {"mensagem" : "Relatorio Recebido"}, 200

#GET Relatorios
@app.route("/relatorio" ,methods=['GET'])
def relatorioGet():
    return jsonify([
        {
            "temperatura": relatorio.temperatura,
            "umidade": relatorio.umidade,
            "pressao": relatorio.pressao,
            "luminosidade": relatorio.luminosidade,
            "qualidade_ar": relatorio.qualidade_ar
        }
        for relatorio in lista_relatorios
    ])

#Rota Padrão
@app.route('/')
def home():
    return render_template('index.html')



#inicia a aplicação flask
app.run()