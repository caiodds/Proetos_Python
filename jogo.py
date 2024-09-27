import random

def jogo_adivinha():
    numero_secreto = random.randint(1,100)
    tentaivas = 10

    print("Ola bem vindo ao jogo")
    print("Tente adivinhar o numero")

    while tentaivas > 0:
        try:
            palpite = int(input(f"Voce tem {tentaivas} tentativas restantes "))

            if palpite < 1 or palpite > 100:
                print("Digite numero entre 1 e 100: ")
                continue
            if palpite == numero_secreto:
                print(f"Acertou! Voce utilizou {tentaivas} tentativas para acertar")
                break
            if palpite < numero_secreto:
                print("Numero e maior")


            else:
                print("Numero menor")

                tentaivas -=1

        except ValueError:
            print("Insira numero valido")

        if tentaivas == 0:
            print(f"Que pena as tentativas se esgotaram")

jogo_adivinha()
