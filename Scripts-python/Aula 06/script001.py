num1 = int(input ('Digite o primeiro número:'))

num2 = int(input('Digite o segundo número:'))

soma = num1 + num2

print ('A some entre',num1,'+',num2,'é: {}'.format(soma))

#Uma maneira mais fácil para colocar variaveis dentro da string

print ('A soma entre {} e {} equivale a: {}'.format(num1, num2, soma))


l = input ('Digite alguma coisa: ')
print(type(l))

#Para saber se é número ou letra

lo = input ('Digite algo: ')
print(lo.isnumeric())

p = input('Digite algum valor ')
print (p.isalpha())
#para saber se a letra esta em letra maiuscula
m = input('Digite algum valor ')
print (p.isupper())

#para saber se a letra esta em letra minuscula
mi = input('Digite algum valor ')
print (p.isupper())
#ANOTAÇÕES

n1 = str(input('Digite alguma coisa: '))
print(n1)
print (type(n1))

n2 = int(input('Digite alguma coisa: '))
print(n2)
print (type(n2))

n3 = float(input('Digite alguma coisa: '))
print(n3)
print (type(n3))

n4 = bool(input('Digite alguma coisa: '))
print(n4)
print (type(n4))

#tipos primitivos

tp_string = "Olá"
tp_int = 7
tp_float = 10.0
tp_bool = 1 #true

