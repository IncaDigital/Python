print('==== Desafio 4 ===')
#Crie um programa que leia algo pelo teclado e mostre na tela o tipo primitivo e todas as informações posiveis sobre ela.
x = input('Digite algo!!: ')
print('O tipo primitivo desse valor é ', type(x))
print('Só têm espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('É alfanumerico?', x.isalnum())
print('Esta em MAIUSCULAS?', x.isupper())
print('Esta em minusculas?', x.islower())
print('Ésta Capitalizada?', x.istitle())

