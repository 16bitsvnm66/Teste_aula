print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
idade: int = int(input("Qual é a sua idade? "))
print(f"Tu tens {idade} anos...")

if idade >= 18:
    print("És maior de idade!")
else:
    print("És menor de idade!")

cidade = input("Em que cidade vives? ")
print(f"{nome} vive em {cidade}.")

ano_atual = 2026
ano_nascimento = ano_atual - idade
print(f"Provavelmente nasceste em {ano_nascimento}.")

print("Obrigado por participares!")

for i in range(3):
    print(f"Iteração número {i + 1}")

ativo: bool = True
print(f"Estado ativo: {ativo}")

print("Conclusão do programa:")
print("Este programa recolhe dados do utilizador e processa informações básicas.")