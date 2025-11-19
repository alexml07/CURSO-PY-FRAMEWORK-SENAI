# Exercício Aula14 sem Streamlit, usando somente console mesmo

import ExAula14C as p # Importar o modulo

# Entrada de dados Pessoas
print('\nEntre com os dados da 1ª pessoa: ')
nome=input('Nome: ')
idade=int(input('Idade: '))
pes1=p.Pessoa(nome, idade)

print(f'\nEntre com os dados da 2ª pessoa: ')
nome=input('Nome: ')
idade=int(input('Idade: '))
pes2=p.Pessoa(nome, idade)

if pes1.eh_mais_velha(pes2.idade):
    print(f'A pessoa mais velha é: {pes1.nome}')
elif pes2.eh_mais_velha(pes1.idade):
    print(f'A pessoa mais velha é: {pes2.nome}')
else:
    print('As duas pessoas tem a mesma idade.')

# Entrada de dados Funcionários

print('\nEntre com os dados do 1° funcionário: ')
nome=input('Nome: ')
salario=int(input('Salário: '))
fun1=p.Funcionario(nome, salario)

print(f'\nEntre com os dados da 2° funcionário: ')
nome=input('Nome: ')
salario=int(input('Salário: '))
fun2=p.Funcionario(nome, salario)

print(f'O salário médio dos funcionários é: R$ {fun1.salario_medio(fun2.salario):.2f}')