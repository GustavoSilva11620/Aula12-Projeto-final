import mechanics
from random import randint
from time import sleep
import time
vidaMago=50
ManaMago=30
MonstroVida=60
while vidaMago >=0:
    mechanics.menu_combate()
    opcao=int(input())
    if opcao==1:
        mechanics.calcular_dano(randint(1,15))