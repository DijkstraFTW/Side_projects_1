
a, A, b = 0, 1, 0

x = eval(input("Enter the grade of the Fibonacci sequence"))
y = input("Do you want the list of terms before yours ?  (Y/N)")

if y == "Y" :
    while b < x :
        if x <= 0 :
            break
        if x > 0 :
            k = a + A
            a = A
            A = k
        b = b + 1
        print(a)
elif y == "N" :
    while b < x :
        if x <= 0 :
            break
        if x > 0 :
            k = a + A
            a = A
            A = k
        b = b + 1
    print(a)
else:
    print('Ooops!  That was not a valid answer try again...')
input('Press ENTER to exit')   