def simulacao_poupanca():
    saldo = 0
    meses = 0
    investido = 0
    juros = 0

    investimento_mensal = 500
    rendimento_mensal = 0.0005

    while saldo < 1_000_000:

        saldo += investimento_mensal
        investido += investimento_mensal
        

        saldo *= (1 + rendimento_mensal)
        
        meses += 1


        if saldo >= 100000 and juros == 0:
            juros = saldo - investido
            anos100mil, meses100mil = divmod(meses, 12)
            print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
            print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
            print(f"Juros compostos até R$ 100.000,00: R$ {juros:.2f}\n")


    anos_final, meses_final = divmod(meses, 12)
    juros_final = saldo - investido
    print(f"Tempo total para atingir R$ 1.000.000,00: {anos_final} anos e {meses_final} meses")
    print(f"Valor investido até R$ 1.000.000,00: R$ {investido:.2f}")
    print(f"Juros compostos totais: R$ {juros_final:.2f}")