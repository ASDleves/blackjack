#megoldás a metodus alá
def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]

    return ertek

def eredmeny(gep_lapok,jatekos_lapok):
    gepertek = pontszamitas(gep_lapok)
    jatekosertek = pontszamitas(jatekos_lapok)
    if gepertek > 21:
        print("A gép vesztett")
    if jatekosertek > 21:
        print("A játékos vesztett")

#tesztesetek