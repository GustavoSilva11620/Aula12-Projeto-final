
from random import randint










def calcular_dano(ataque,defesa):
    dano=ataque-defesa
    if dano <= 0:
        return 1
    else:
        return dano
def usarpocao(vida_atual):
    vida_atual+=15
    if vida_atual >50:
        vida_atual=50
        return vida_atual
def  menu_combate():
    print(f"Escolha a sua opcao:\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1-Ataque\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n2-Cura\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n3-Fugir")


