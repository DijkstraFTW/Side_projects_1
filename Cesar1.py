code = input("Enter the text to decipher")
key = eval(input("Enter your top-secret key"))
for l in code :
    pu = ord(l) + key
    if pu < 97 :
        pu = pu + 25
    if pu > 122 :
        pu = pu - 25
    if ord(l) == 32 :
        pu = ord(l)
    print(chr(pu), end='')
input('Press ENTER to exit')
