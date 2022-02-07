print("**************************************")
print("Seja bem vindo ao Jogo de Adivinhação!")
print("**************************************")

numero_secreto = 42
total_de_tentativas = 3


for tentativa_atual in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(tentativa_atual, total_de_tentativas))
    chute_str = input("Digite o seu palpite: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1  or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto 
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você ACERTOU!!")
        break
    else: 
        if(maior):
            print("Você errou. Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou. Seu chute foi menor que o número secreto")

print("Fim do jogo")