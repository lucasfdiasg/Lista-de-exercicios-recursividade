import sys
sys.setrecursionlimit(20000)  # Aumenta o limite de recursão

def simulacao_poupanca(saldo=0,
                       carteira_btc=0
                       meses=0,
                       investido=0,
                       investimento_mensal=250,
                       indice = 0):
    

    lista_de_valores_bitcoin_2024 = [210500, 258614, 345835, 335892, 316822, 372548,\
                                     364703, 339004, 348167, 385298, 440983, 636069]
    
    if indice > 11:
        indice = 0

    # Base da Recursão: Quando atingir R$ 1.000.000,00
    if saldo >= 1_000_000:
        anos_final, meses_final = divmod(meses, 12)


        print(f"Tempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
        print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
        return

    #Conversão para BTC
    anos_final, meses_final = divmod(meses, 12)
    
    investimento_em_btc += investimento_mensal/lista_de_valores_bitcoin_2024[indice]

    # Adiciona o investimento mensal
    carteira_btc += investimento_em_btc
    investido += investimento_mensal

    meses += 1  # Passa um mês

    # Se atingir R$ 100.000 pela primeira vez, armazena o valor dos juros
    if saldo >= 100_000 and juros100k is None:
        juros100k = saldo - investido
        anos100mil, meses100mil = divmod(meses, 12)
        print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
        print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
    indice += 1
    # Chamada recursiva
    simulacao_poupanca(saldo,
                       meses,
                       investido,
                       juros100k,
                       investimento_mensal,
                       rendimento_mensal,
                       indice)


# Executa a simulação
simulacao_poupanca()