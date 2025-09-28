import funcoes as f

'''
Esse programa solicita ao usúario dois números 
e exibe na tela as quatros operações basicas.
Exemplo: 5 e 8
Adição: 5 + 8 = 13
Subtração: 5 - 8 = -3
Multiplicação: 5 x 8 = 40
Divisão: 5 / 8 = 0.625
'''

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print(f'Adição: {numero1} + {numero2} = {f.adicao(numero1, numero2)}')
print(f'Subtração: {numero1} - {numero2} = {f.subtracao(numero1, numero2)}')
print(f'Multiplicação: {numero1} x {numero2} = {f.multiplicacao(numero1, numero2)}')
print(f'Divisão: {numero1} / {numero2} = {f.divisao(numero1, numero2)}')