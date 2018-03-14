p = input("Insérer le texte à déchiffrer")
for l in p :
    pu = ord(l) - 109
    pn = 109 - ord(l)
    if ord(l) < 109 :
        l = l + chr(2 * pu)
    if ord(l) > 109 :
        l = l - chr(2 * pu)
    if ord(l) == 109 :
        l = l + 1
input('Press ENTER to exit')                
