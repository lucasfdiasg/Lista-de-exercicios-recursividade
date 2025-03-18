import sys
sys.setrecursionlimit(20000)  # Aumenta o limite de recursão

def simulacao_poupanca(saldo=0,
                       meses=0,
                       investido=0,
                       juros100k=None,
                       investimento_mensal=500,
                       rendimento_mensal=0.0005,
                       indice = 0):
    

    lista_de_valores_do_dollar_2024 = [4.85, 4.97, 4.95, 5.07, 5.08, 5.11, 5.65, 5.72 ,5.50, 5.45, 5.76, 6.17]
    if indice > 11:
        indice = 0

    # Base da Recursão: Quando atingir R$ 1.000.000,00
    if saldo >= 1_000_000:
        anos_final, meses_final = divmod(meses, 12)
        juros_final = saldo - investido


        print(f"Tempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
        print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
        print(f"Juros compostos totais: R$ {juros_final:.2f}")
        return

    # Adiciona o investimento mensal
    saldo += investimento_mensal
    investido += investimento_mensal

    #Conversão para dóllar
    anos_final, meses_final = divmod(meses, 12)
    
    saldo_em_dol = saldo/lista_de_valores_do_dollar_2024[indice]

    # Aplica os juros compostos de 0,05%
    saldo_em_dol += saldo_em_dol*rendimento_mensal

    saldo = saldo_em_dol*lista_de_valores_do_dollar_2024[indice] 

    meses += 1  # Passa um mêis

    # Se atingir R$ 100.000 pela primeira vez, armazena o valor dos juros
    if saldo >= 100_000 and juros100k is None:
        juros100k = saldo - investido
        anos100mil, meses100mil = divmod(meses, 12)
        print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
        print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
        print(f"Juros compostos até R$ 100.000,00: R$ {juros100k:.2f}\n")
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