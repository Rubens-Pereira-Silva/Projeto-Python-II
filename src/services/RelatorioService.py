from src.data.database import db
from models.RelatorioDB import RelatorioDB

#POST Relatorio
def RelatorioPOST(dados):
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
    return {"mensagem" : "Relatorio Recebido"}, 201