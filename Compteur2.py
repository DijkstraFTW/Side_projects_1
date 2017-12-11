p = input("Enter the letter to use")
nb = 0 # Compteur 1 
for l_ in p :
    if l_ != " " :
        nb_ = 0
        for l in p :
            if l_ == l :
                nb_ = nb_ +1
        if nb_ > nb :
            lettreMaxi = l_
            nb = nb_
print(lettreMaxi, nb, sep =' ')