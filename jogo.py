import mechanics
from random import randint
from time import sleep
import time
vidaMago=50
ManaMago=30
MonstroVida=60
mechanics.menu_combate()
while vidaMago >=0 and MonstroVida >=0:
    opcao=int(input())
    if opcao==1:
        if ManaMago>5:
            print("A conjurar",end="",flush=True)
            dano=mechanics.calcular_dano(randint(10,20,),5)
            for x in range(1,3):
                sleep(0.5)
                print(".",end="",flush=True)
            MonstroVida-=dano
            print(f"Bom trabalho!Deste {dano} de dano ao monstro! Ele esta agr com {MonstroVida} de hp!Tas com{ManaMago} de mana")
        else:
            print(f"Mana insuficiente! Tens {ManaMago} de Mana!!")
    elif opcao==2:
        if ManaMago>10:
            vidaMago=mechanics.usarpocao(vidaMago)
            print(f"Mago usa pocao! Mago recupera 15 de hp! Vida: {vidaMago}")
        else:
            print(f"Mana insuficiente! Tens {ManaMago} de Mana!!")
    elif opcao==3:
        print("Fugiste wow....Que divertido que foi ne :/ VOLTA A JOG")
        break
    else :
        print("Opcao invalida!")
    if MonstroVida>0:
        danM=mechanics.calcular_dano(randint(10,25),5)
        vidaMago-=danM
        print(f"Montro atacou!!Dano:{danM} Vida: {vidaMago}")
    if MonstroVida<0:
        print("MAGO GANHOU A BATALHAAAAAAAAAAAAAAAAA yay")
    if vidaMago<0:
        print("Mago perdeu ToT")




