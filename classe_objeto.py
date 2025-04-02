#Abordagem : Usando Classes e Objetos

class Aluno:
    def __init__(self, nome, idade, altura, aprovado):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.aprovado = aprovado

    def exibir_dados(self):
        print("\nDados do aluno:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Altura:", self.altura)
        print("Aprovado:", "Sim" if self.aprovado else "Não")

# Criando um objeto Aluno
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
altura = float(input("Digite a altura do aluno (em metros): "))
aprovado = input("O aluno foi aprovado? (sim/não): ").lower() == "sim"

aluno = Aluno(nome, idade, altura, aprovado)
aluno.exibir_dados()
