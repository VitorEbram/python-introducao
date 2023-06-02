print("**************************************")
print("****** Adivinhe qual é o número ******")
print("**************************************")

NUMERO_SECRETO = 83
tentativa = input("Tente acertar o número: ")
print("Você digitou: ", tentativa)

try:
    tentativa_int = int(tentativa)
except ValueError:
    print("Valor inválido. Informe um número inteiro")
    exit()

tentativa_int = int(tentativa)

if (NUMERO_SECRETO == tentativa_int):
    print("ACERTOU!")
else:
    print("Você errou!")
    
print("GAME OVER!")
print("Obrigado por jogar!")