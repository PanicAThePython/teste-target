palavra = input("String para inverter... ")
invertido = ""

for index in reversed(range(len(palavra))):
    invertido+=palavra[index]

print(invertido)