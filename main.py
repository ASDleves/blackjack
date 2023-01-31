#megoldás a metodus alá
def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]

    return ertek

def eredmeny(gep_lapok,jatekos_lapok):
    gepertek = pontszamitas(gep_lapok)
    jatekosertek = pontszamitas(jatekos_lapok)
    eredmeny = ""
    if gepertek > 21:
        eredmeny = "A gép vesztett"
    elif jatekosertek > 21:
        eredmeny = "A játékos vesztett"
    else:
        eredmeny = "ház vesztett"
    return eredmeny

def jatekosvesztett_teszt():
    jatekos = [10,10,5]
    gep = [5,10]
    vart_eredmeny = "A játékos vesztett"
    kapott_eredmeny = eredmeny(jatekos,gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("teszt megbukott")

def teszt_tesztesetek():
    jatekosvesztett_teszt()
teszt_tesztesetek()



#tesztesetek