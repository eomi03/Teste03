#salario_atual = float(input("Digite o salário mensal atual do funcionário: "))
#porcentagem_reajuste = float(input("Digite o percentual de reajuste (apenas o número, sem o símbolo %): "))

#valor_reajuste = salario_atual * (porcentagem_reajuste/100)
#novo_salario = salario_atual + valor_reajuste

#print(f"O valor do novo salário é: R$ {novo_salario:.2f}")





#preco_litro = float(input("Digite o preço do litro do combustível: "))
#desempenho = float(input("Digite o desempenho do veículo em km/l: "))
#distancia = float(input("Digite a distância entre as duas cidades em km: "))

#litros_necessarios = distancia / desempenho
#valor_gasto = litros_necessarios * preco_litro

#print(f"Serão necessários {litros_necessarios:.2f} litros de combustível e o valor gasto será R${valor_gasto:.2f}.")

total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

percentual_brancos = votos_brancos * 100 / total_eleitores
percentual_nulos = votos_nulos * 100 / total_eleitores
percentual_validos = votos_validos * 100 / total_eleitores

print("Percentual de votos brancos: %.2f%%" % percentual_brancos)
print("Percentual de votos nulos: %.2f%%" % percentual_nulos)
print("Percentual de votos válidos: %.2f%%" % percentual_validos)






