"""Abordagem  Usando Dicionários
Outra forma é armazenar os dados do aluno em dicionário, o que é útil 
para manipular dados de forma estruturada."""

aluno = {}
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["idade"] = int(input("Digite a idade do aluno: "))
aluno["altura"] = float(input("Digite a altura do aluno (em metros): "))
aluno["aprovado"] = input("O aluno foi aprovado? (sim/não): ").lower() == "sim"

print("\nDados do aluno:")
for chave, valor in aluno.items():
    if chave == "aprovado":
        print(chave.capitalize() + ":", "Sim" if valor else "Não")
    else:
        print(chave.capitalize() + ":", valor)
