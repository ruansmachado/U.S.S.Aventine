# Contém as funções do jogo Star Trek: Destiny
import sys
import time


pessoal = 750
vida = {'escudo': 100}


def vida_atua():
    vida_atual = vida['escudo']
    if vida_atual > 0:
        print(f"Seu escudo está {vida['escudo']}%!")
    elif vida['escudo'] <= 0:
        print('Sua nave foi destruida... Você perdeu!')
        sys.exit()


def tripulação(baixas):
    baixas_sofrida = pessoal - baixas
    pessoal_atual = baixas_sofrida
    if pessoal > baixas:
        print(
            f"{baixas} tripulantes foram perdidos. A tripulação atual está em {pessoal_atual}!")
    elif pessoal < baixas:
        print(f"Você perdeu toda a tripulação e sua nave inicio procedimento de autodestruição.")
        print("Você perdeu...")
        sys.exit()


def rot(word):  # Se desejar aumentar a velocidade do texto, é só alterar para (0)
    for i in word:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0)
