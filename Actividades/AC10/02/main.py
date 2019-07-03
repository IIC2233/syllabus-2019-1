import parametros as p
from personas import DrHenry, Progravenger

def crear_instancias():
    drhenry = DrHenry(p.H_VIDA, p.H_ATAQUE)
    astark = Progravenger(p.A_VIDA, p.A_FUERZA, p.A_ARMA, p.A_NOMBRE)
    cruz = Progravenger(p.C_VIDA, p.C_FUERZA, p.C_ARMA, p.C_NOMBRE)
    vichor = Progravenger(p.V_VIDA, p.V_FUERZA, p.V_ARMA, p.V_NOMBRE)
    return drhenry, (astark, cruz, vichor)

def simular(henry, progravengers):
    while henry.vida > 0 and sum(avenger.vida for avenger in progravengers) > 0:
        for avenger in progravengers:
            if avenger.vida > 0:
                avenger.atacar(henry)
            if henry.vida == 0:
                break
            henry.atacar(avenger)
    if sum(avenger.vida for avenger in progravengers) == 0:
        print("DrHenry derroto a los Progravengers")


if __name__ == "__main__":
    henry, progravengers = crear_instancias()
    simular(henry, progravengers)