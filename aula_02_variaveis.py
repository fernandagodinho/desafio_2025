"""insira e exiba os dados de um aluno incluindo nome, idade, altura e se o aluno foi 
aprovado ou nao . usamos diferentes tipos de dados para armazenar essas 
informaçoes str  para o nome , int para idade , float para altura e bool para  a aprovaçao"""

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
altura = float(input("Digite a altura do aluno: "))
aprovado = input("O aluno foi aprovado? (sim/não): ").lower() == "sim"

# Exibir dados do aluno
print("\nDados do aluno:")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Aprovado:", "Sim" if aprovado else "nao")