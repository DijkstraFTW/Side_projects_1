def CesarAuto() :
    p = input("Entrez le texte à déchiffrer")
    nb = 0 # Compteur 1 
    for l_ in p :
        if l_ != " " :
            nb_ = 0
            for l in p :
                if l_ == l :
                    nb_ = nb_ + 1
            if nb_ > nb :
                lettreMaxi = l_
                nb = nb_
    print(lettreMaxi, nb, sep =' ')
    for i in p :
        nb = 101 - ord(lettreMaxi)
        pu = ord(i) + nb
        if pu < 97 :
            pu = pu + 25
        if pu > 122 :
            pu = pu - 25
        if ord(i) == 32 :
            pu = ord(i)
        print(chr(pu), end='')
CesarAuto()
input('Press ENTER to exit')