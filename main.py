#megoldás a metodus alá
def pontszamitas(gep_lap,jatekos_lap):
    gepertek = 0
    jatekosertek = 0
    for i in range(len(gep_lap)):
        gepertek += gep_lap[i]
    for i in range(len(jatekos_lap)):
        gepertek += jatekos_lap[i]


def eredmeny(gepertek,jatekosertek):
    if gepertek > 21:
        print("A gép vesztett")
    if jatekosertek > 21:
        print("A játékos vesztett")

#tesztesetek