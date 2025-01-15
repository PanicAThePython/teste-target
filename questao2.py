numero = int(input("Informe um número int... "))


def ehFibonacci(num):
    fibAtual = [0, 1, 1]
    indexAtual = 2
    enFibo = False
    while fibAtual[indexAtual] <= num:
        soma = fibAtual[indexAtual] + fibAtual[indexAtual-1]
        fibAtual.append(soma)
        if (soma == num):
            ehFibo = True
            return "Faz parte de fibonacci"
        indexAtual+=1
    return "Não pertence a sequencia"

if (numero == 0 or numero ==1):
    print("Está na sequência de fibonacci")
else:
    print(ehFibonacci(numero))