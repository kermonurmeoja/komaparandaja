vigane = []
i = 0
fail = open("vigane.txt", encoding="UTF-8")
for rida in fail:
    vigane.append(str(rida))
fail.close()

def paranda(laus):
    laus = lause1.replace(" aga ", ", aga ")
    laus = laus.replace(" sest ", ", sest ")
    laus = laus.replace(" et ", ", et ")
    laus = laus.replace(" ent ", ", ent ")
    return laus

while i < len(vigane):
    lause1 = vigane[i].strip()
    parandatud = paranda(lause1)
    f = open("parandatud.txt", "a") ## Lisasin a, kuna seda on mugavam while'iga kasutada.
    f.write(parandatud + "\n")
    f.close()
    i = i + 1