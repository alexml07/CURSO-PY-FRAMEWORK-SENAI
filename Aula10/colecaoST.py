# Lista em Python
# Indices 0      1    2    3
lista=["Senai", True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[2])
print(len(lista))
lista.insert(1,"Campeao")
lista.append("Feriado")
del lista[3]
lista.append("Senai")
for i in range(len(lista)):
    print(lista[i])

# Tupla
tupla=("Senai", True, 56, 74.6)
print(tupla)
print(type(tupla))
print(tupla[3])
print(tupla[1])
TUPLA=('Senai', True, 56, 74.6, 56)
print(TUPLA)
print(tupla)

# Dicionario
dicionario={'nome':'Senai','logica': False, 'num1':2, 'num2': 1.5}
print(dicionario)
print(type(dicionario))
print(dicionario['logica'])
for chave in dicionario.keys():
    print(chave, '->', dicionario[chave])
dicionario.update({'novo': 'Senai'})
dicionario.update({'nome': 'Terça'})
del dicionario['logica']

# Conjunto
conjunto={'Senai', False, 10, 2.69, True, 3}
print(conjunto)
print(type(conjunto))
conjunto.add(23)
conjunto.discard('Senai')
conjunto.add('Senai')
conjunto.add('Senai')
conjunto.clear()