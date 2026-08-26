class RelatorioRecebido:
    #Construtor
    def __init__(
        self,
        temperatura,
        umidade,
        pressao,
        luminosidade,
        qualidade_ar
    ):
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao
        self.luminosidade = luminosidade
        self.qualidade_ar = qualidade_ar
