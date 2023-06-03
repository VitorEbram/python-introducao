from os import system
from random import randint
system("cls")

print("Adivinhe qual é o número")

numero_secreto = randint(0,100)

pontos = 1000
acerto = False

print("Qual o nível de dificuldade?")
print("(1) Padawan\n(2) Cavaleiro\n(3) Mestre Jedi")
nivel = int(input("\nDefina o nivel: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else: 
    total_de_tentativas = 5

pontos_a_perder = int(pontos / total_de_tentativas)
print(f"Sua pontuação atual: {pontos}")

for rodada in range (1, total_de_tentativas+1):
    tentativa = input("Tente acertar o número: ")
    print("Você digitou: ", tentativa)
    print(f"\nTentativa {rodada:02d} de {total_de_tentativas:02d}")
    
    try:
        tentativa_int = int(tentativa)
    except ValueError:
        print("Valor inválido. Informe um número inteiro")
        exit()
    except Exception as e:
        print(f"ERRO {e}")
        exit()
    else:
        pass
    finally:
        pass

    if (tentativa_int < 1 or tentativa_int > 100):
        print("Tentativa inválida! Somente números de 1 a 100")
        continue

    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    if acerto:
        print(f"PARABÉNS, VOCÊ ACERTOU!!\nVocê fez {pontos} pontos")
        break      
    else:
        pontos_proximidade = 50 - abs(numero_secreto - tentativa_int)
        pontos = pontos - pontos_a_perder + pontos_proximidade
        if ehmaior:
            print("Sua tentativa foi MAIOR que o número secreto.")
            print()
        if ehmenor:
            print("Sua tentativa foi MENOR que o número secreto.")
            print()
        if (rodada < total_de_tentativas):
            print(f"Sua pontuação atual: {pontos}")
if not acerto:        
    print(f"GAME OVER! O número era {numero_secreto}!")
print("Obrigado por jogar!")