from datetime import datetime

class Conta:
    def __init__(self,n_Conta:str='',dataLeitura:datetime=datetime.now(),n_Leitura:str='',kw_Gasto:int=0,valor_Pagar:float = 0.0,dataPagamento:datetime=datetime.now())-> None:
        self.__n_Conta = n_Conta
        self.__dataLeitura = dataLeitura
        self.__n_Leitura = n_Leitura
        self.__kw_Gasto = kw_Gasto
        self.__valor_Pagar = valor_Pagar
        self.__dataPagamento = dataPagamento
    
    def getDataLeitura(self):
        return self.__dataLeitura.strftime(" %d %m %Y")

    def getDataPagamento(self):
        return self.__dataPagamento.strftime(" %d %m %Y")

    def getKwGasto(self) -> int:
        return self.__kw_Gasto

    def getValorPagar(self) -> float:
        return self.__valor_Pagar

    def getDadosConta(self) -> str:
        return f"Conta: {self.__n_Conta}, Conta: {self.__dataLeitura}, Conta: {self.__n_Leitura}, Conta: {self.__kw_Gasto}, Conta: {self.__valor_Pagar}, Conta: {self.__dataPagamento}"