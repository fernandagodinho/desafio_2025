# Algoritmo para verificar se a pessoa pode entrar no parque de diversões
def verificar_entrada_parque():
    # Solicitar altura da pessoa
    altura = float(input("Informe a sua altura em metros: "))
    
    # Verificar se a altura é maior ou igual a 1,40 metros
    if altura >= 1.40:
        print("Você pode entrar no parque de diversões!")
    else:
        print("Você não pode entrar no parque de diversões.")

# Chamar a função
verificar_entrada_parque()



""""Passo 1: Algoritmo em Linguagem Natural 

  

1. O algoritmo começa perguntando à pessoa a sua altura. 


2. O algoritmo verifica se a altura da pessoa é maior ou igual a 1,40 metros. 

  

Se a altura for maior ou igual a 1,40 metros, a pessoa pode entrar no parque de diversões. 

  

Se a altura for menor que 1,40 metros, a pessoa não pode entrar no parque de diversões. 

  
3. O algoritmo termina. 

  

 ----------------------------------------------------------------------------------- 
Passo 2: Fluxograma 


  

1. Início: O processo começa. 

2. Entrada da altura: A pessoa informa a sua altura. 

3. Verificar altura: O algoritmo compara a altura com 1,40 metros. 

Se a altura for maior ou igual a 1,40m, vá para a etapa "Pode entrar". 

Se a altura for menor que 1,40m, vá para a etapa "Não pode entrar". 

4. Pode entrar: O algoritmo informa que a pessoa pode entrar no parque. 

5. Não pode entrar: O algoritmo informa que a pessoa não pode entrar no parque. 

6. Fim: O processo termina. 

  ------------------------------------------------- 

 

Passo 3: Algoritmo em Pseudocódigo 

Algoritmo: Verificar_Entrada_Parque 

  

Início 

    Leia altura 

    Se altura >= 1.40 então 

        Escreva "Você pode entrar no parque de diversões!" 

    Senão 

        Escreva "Você não pode entrar no parque de diversões." 

    FimSe 

Fim 

  

 """