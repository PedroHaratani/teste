from .Conta import Conta

class Contas:
    def __init__(self) -> None:
        self.self__contas = []
    
    def getMediaKw(self) -> int:
        soma = 0
        for i in range(len(self.self__contas)):
            c = Conta()
            c = self.self__contas[i]
            soma += c.getKwGasto()
        return soma//len(self.self__contas)

            

    def getValorMediaContas(self) -> int:
        soma = 0
        for i in range(len(self.self__contas)):
            c = Conta()
            c = self.self__contas[i]
            soma += c.getValorPagar()
        return soma//len(self.self__contas)

    def getMesMaiorConsumo(self):
        maior = 0
        data = ""
        for i in range(len(self.self__contas)):
            
            if self.self__contas[i].getKwGasto() > maior:
                maior = self.self__contas[i].getKwGasto()
                data = self.self__contas[i].getDataPagamento()
        return data 

    def getMesMenorConsumo(self):
        menor = 0
        data = ""
        for i in range(len(self.self__contas)):
            
            if i == 0:
                menor = self.self__contas[i].getKwGasto()

            if self.self__contas[i].getKwGasto() < menor:
                menor = self.self__contas[i].getKwGasto()
                data = self.self__contas[i].getDataPagamento()

        return data

    def getContas(self):
        contas = []
        for i in range(0,len(self.self__contas)):
            if self.self__contas[i].getDadosConta() is not None:
                contas.append(self.self__contas[i].getDadosConta())
            
        return contas

    def setConta(self,conta:Conta):
        self.self__contas.append(conta)