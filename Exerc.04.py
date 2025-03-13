def simulacao_poupanca(saldo=0, meses=0, investido=0, juros100k=0, investimento_mensal=500, rendimento_mensal=0.0005):
# Verifica se já atingimos 1 milhão, caso sim, encerramos a recursão
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
# Aplica os juros compostos de 0,05%
    saldo *= (1 + rendimento_mensal)

    meses += 1  # Passa um mês
# Se atingir 100k pela primeira vez, registra os dados
    if saldo >= 100_000 and juros100k == 0:
        juros100k = saldo - investido
        anos100mil, meses100mil = divmod(meses, 12)
        print(f"Tempo para atingir R$ 100.000,00: {anos100mil} anos e {meses100mil} meses")
        print(f"Valor investido até R$ 100.000,00: R$ {investido:.2f}")
        print(f"Juros compostos até R$ 100.000,00: R$ {juros100k:.2f}\n")

# Chamada recursiva
    simulacao_poupanca(saldo, meses, investido, juros100k, investimento_mensal, rendimento_mensal)