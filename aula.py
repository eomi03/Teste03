days = str(input("insira a quantidade de dias:"))
hr = int(input("Insira as horas:"))
min = int(input("Insira os minutos:"))
seg = int(input("Insira os segundos:"))

segtotal = days*86400*hr*3600*min*60*seg*60
print(str(input(f"o total é,{segtotal}")))