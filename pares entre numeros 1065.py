lista = []
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())
lista.append(v1)
lista.append(v2)
lista.append(v3)
lista.append(v4)
lista.append(v5)
cont = 0
for i in lista:
    if i % 2 == 0:
        cont =cont + 1
print('{} valores pares'.format(cont))
    

