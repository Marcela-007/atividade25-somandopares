# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
numeroo = []
for number in range(0,6):
 numeros = int(input('Digite seis números:'))
 if numeros % 2==0:
  numeroo.append(numeros)
 soma = sum(numeroo)
 print(soma)
else:
 print('Não há números pares nos números informados')