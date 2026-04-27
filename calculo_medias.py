# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Função para calcular média
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# Função para verificar aprovação
def verificar_aprovacao(media):
    if media >= 7:
        aprovacao = "Aprovado!"
    elif media >= 5:
        aprovacao = "Reprovado, aguarde a recuperação."
    return aprovacao

# Função de relatório
def relatorio_final(nome, media, aprovacao):
    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {aprovacao}")

# Processamento dos dados
media = calcular_media(nota1, nota2)
aprovacao = verificar_aprovacao(media)

# Saída de dados
relatorio_final(nome, media, aprovacao)