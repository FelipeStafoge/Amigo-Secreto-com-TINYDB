from random import choice
from tinydb import TinyDB

db = TinyDB('db.json')

pessoa = {}


def menu():
    print('1- Ver Lista de Participantes\n2- Cadastrar Pessoas\n3- Apagar Pessoas\n4- Sorteio\n5- Sair')
    while True:
        resp = int(input("Digite o que deseja fazer: "))
        if 0 < resp <= 5:
            break
        else:
            print("Digite um número de 1 até 5!")
    if resp == 1:
        lista()
        menu()
    if resp == 2:
        cadastro()
    if resp == 3:
        remover()
    if resp == 4:
        sorteio()
    if resp == 5:
        print('Encerrando...')


def lista():
    num = 0
    print()
    for i in db.all():
        print(f"ID: {db.all()[num]['ID']}  Nome: {db.all()[num]['nome']} Presente: {db.all()[num]['presente']} | ", end='')
        num += 1
    print()


def cadastro():
    cont = len(db.all()) + 1
    while True:
        pessoa["ID"] = cont
        pessoa['nome'] = str(input("Nome: "))
        pessoa['presente'] = str(input("Presente: "))
        db.insert(pessoa.copy())
        pessoa.clear
        cont += 1
        resp = str(input('Continuar? (S/N) '))[0].upper()
        if resp == 'N':
            print()
            menu()
            break


def remover():
    lista()
    resp = int(input("Deseja apagar qual? <999 para cancelar e voltar pro menu!> "))
    if resp == 999:
        menu()
    else:
        db.remove(doc_ids=[resp])
        print('Apagado com SUCESSO!')
        menu()


def sorteio():
    listaid = []
    soma = 0
    for i in db.all():
        listaid.append(db.all()[soma]['ID'])
        soma += 1
    sorte = choice(listaid) - 1
    print(listaid)
    print(f"O sorteado foi {db.all()[sorte]['nome']} e o que ele quer de presente é um/a {db.all()[sorte]['presente']}")
    menu()


menu()