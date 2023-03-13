salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
porcentagem_reajuste = float(input("Digite o percentual de reajuste (apenas o número, sem o símbolo %): "))

valor_reajuste = salario_atual * (porcentagem_reajuste/100)
novo_salario = salario_atual + valor_reajuste

print(f"O valor do novo salário é: R$ {novo_salario:.2f}")