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

