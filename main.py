import funcoes as f

'''
Esse programa solicita ao opções de conversão (Celius, Fahrenheit ou Kelvin) e um valor a ser convertido, em seguida exibi na tela o resultado.
'''

print('1: Celius')
print('2: Fahrenheit')
print('3: Kelvin')
a_ser_convertido = int(input('Digite a ser convertido: '))
convertido = int(input('Digite para qual vai ser convertido: '))
temp = float(input('Digite o valor a ser convertido: '))
if a_ser_convertido == 1 and convertido == 2:
    resultado = f.celsius_fahrenheit(temp)
elif a_ser_convertido == 1 and convertido == 3:
    resultado = f.celsius_kelvin(temp)
elif a_ser_convertido == 2 and convertido == 1:
    resultado = f.fahrenheit_celsius(temp)
elif a_ser_convertido == 2 and convertido == 3:
    resultado = f.fahrenheit_kelvin(temp)
elif a_ser_convertido == 3 and convertido == 1:
    resultado = f.fahrenheit_kelvin(temp)
elif a_ser_convertido == 3 and convertido == 2: 
    resultado = f.kelvin_fahrenheit(temp)
else:
    resultado = print('Digite valores válidos!')
print(f'Resultado: {resultado:.2f}')