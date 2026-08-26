from flask import Flask, render_template

#Cria a aplicação flask
app = Flask(__name__)

#Rotas

#Rota Padrão
@app.route('/')
def home():
    return render_template('index.html')

#inicia a aplicação flask
app.run()