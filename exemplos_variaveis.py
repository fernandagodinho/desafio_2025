def obter_dados_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    altura = float(input("Digite a altura do aluno (em metros): "))
    aprovado = input("O aluno foi aprovado? (sim/não): ").lower() == "sim"
    return nome, idade, altura, aprovado

def exibir_dados_aluno(nome, idade, altura, aprovado):
    print("\nDados do aluno:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Altura:", altura)
    print("Aprovado:", "Sim" if aprovado else "Não")

# Chamando as funções
dados = obter_dados_aluno()
exibir_dados_aluno(*dados)
