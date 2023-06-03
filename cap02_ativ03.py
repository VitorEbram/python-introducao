from os import system
system('cls')

print("**************************************")
print("****** Adivinhe qual é o número ******")
print("**************************************")

NUMERO_SECRETO = 83


total_de_tentativas = 3
acerto = False

for rodada in range (1, total_de_tentativas+1):
    #print(f"Rodada {rodada}")
    tentativa = input("Tente acertar o número: ")
    print("Você digitou: ", tentativa)
    #rodada += 1

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

    acerto = tentativa_int == NUMERO_SECRETO
    ehmaior = tentativa_int > NUMERO_SECRETO
    ehmenor = tentativa_int < NUMERO_SECRETO

    if acerto:
        print(f"PARABÉNS, VOCÊ ACERTOU em {rodada:02d} rodadas!")
        break      
    else:
        if ehmaior:
            print("Sua tentativo foi MAIOR que o número secreto.")
            print()
        if ehmenor:
            print("Sua tentativa foi MENOR que o número secreto.")
            print()
if not acerto:        
    print("GAME OVER!")
print("Obrigado por jogar!")