#megoldás a metodus alá
def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]

    return ertek

def eredmeny(jatekos_lapok,gep_lapok):
    gepertek = pontszamitas(gep_lapok)
    jatekosertek = pontszamitas(jatekos_lapok)
    if gepertek > 21:
        eredmenykiir = "A gép vesztett"
    elif jatekosertek > 21:
        eredmenykiir = "A játékos vesztett"
    elif gepertek > jatekosertek and gepertek <21:
        eredmenykiir = "A játékos vesztett"
    elif gepertek == jatekosertek and gepertek <21 and len(gep_lapok) < len(jatekos_lapok):
        eredmenykiir = "A játékos vesztett"
    else:
        eredmenykiir = "ház vesztett"
    return eredmenykiir

def jatekosvesztettnagyobbertekkel_teszt():
    jatekos_lapok = [10,10,5,]
    gep_lapok = [5,10]
    vart_eredmeny = "A játékos vesztett"
    kapott_eredmeny = eredmeny(jatekos_lapok,gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("teszt megbukott")
def jatekosvesztettkisebbertekkel_teszt():
    jatekos_lapok = [10,5]
    gep_lapok = [10,10]
    vart_eredmeny = "A játékos vesztett"
    kapott_eredmeny = eredmeny(jatekos_lapok,gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("teszt megbukott")
def jatekosvesztettkevesebblappal_teszt():
    jatekos_lapok = [10,5,5]
    gep_lapok = [10,10]
    vart_eredmeny = "A játékos vesztett"
    kapott_eredmeny = eredmeny(jatekos_lapok,gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("teszt megbukott")

def teszt_tesztesetek():
    print("A játékos vesztett teszt(nagyobb ertekkel): ", end="")
    jatekosvesztettnagyobbertekkel_teszt()
    print("A játékos vesztett teszt (kisebb értékkel): ",end="")
    jatekosvesztettkisebbertekkel_teszt()
    print("A játékos vesztett teszt (kevesebb lappal): ",end="")
    jatekosvesztettkevesebblappal_teszt()

teszt_tesztesetek()


