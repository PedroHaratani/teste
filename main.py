from Classes import Conta,Contas
from datetime import datetime

if __name__ == "__main__":
    hContas = Contas()
    

    hContas.setConta(Conta('321312312',datetime.now(),'312313444',250,95.31,datetime.strptime('16/05/2023','%d/%m/%Y')))
    hContas.setConta(Conta('321312312',datetime.now(),'312313444',230,93.31,datetime.strptime('16/06/2023','%d/%m/%Y')))
    hContas.setConta(Conta('321312312',datetime.now(),'312313444',200,80.31,datetime.strptime('16/07/2023','%d/%m/%Y')))

    print(hContas.getMediaKw())
    print(hContas.getMesMaiorConsumo())
    print(hContas.getMesMenorConsumo())
    print(hContas.getValorMediaContas())
    for c in hContas.getContas():
        print(c)
