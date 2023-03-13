days = int(input("insira a quantidade de dias:"))
hr = int(input("insira a quantidade de horas:"))
min = int(input("insira a quantidade de minutos:"))
seg = int(input("insira a quantidade:"))

segtotal = days*86400+hr*3600+min*60+seg
print(f"o total de segundos é,{segtotal}")