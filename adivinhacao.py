#Programa em que o usuário adivinha um número gerado randomicamente pelo código

import random

def tentativa(x):
    num_aleatorio = random.randint(1, x)
    n = 0
    while n != num_aleatorio:
        n = (int(input("Em que número estou pensando?")))

        if n > num_aleatorio:
            print("Tente novamente, com um número menor!")

        elif n < num_aleatorio:
            print("Tente novamente, com um número maior!")

    print("Parabéns você acertou!")

