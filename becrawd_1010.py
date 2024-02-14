a = input().split(" ")
b = input().split(" ")

cod1, qtdel1, valor1 = a
cod2, qtdel2, valor2 = b

total = (int(qtdel1) * float(valor1) + int(qtdel2) * float(valor2))

print(f'VALOR A PAGAR: R$ {total:.2f}')

