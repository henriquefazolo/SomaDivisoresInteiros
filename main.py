n = int(input('Insira o valor de um numero inteiro : \n'))
soma = 0
for i in range(n):
    divisor = i+1
    dividendo = n

    if dividendo % divisor == 0:
        soma += dividendo / divisor

print(soma)
