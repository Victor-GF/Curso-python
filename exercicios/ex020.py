from random import shuffle

aluno1 = input("->  Aluno 1: ")
aluno2 = input("->  Aluno 2: ")
aluno3 = input("->  Aluno 3: ")
aluno4 = input("->  Aluno 4: ")

# Gera a lista de alunos
lista = [aluno1, aluno2, aluno3, aluno4]
# Embaralha a lista
shuffle(lista)

print(">> A ordem dos alunos será:", *lista)

