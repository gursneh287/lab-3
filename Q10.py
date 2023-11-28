x = int(input('enter number 1: '))
y = int(input('enter number 2: '))
z = int(input('enter number 3: '))
if x<y and x<z:
    if y>z:
        print(y)
    else:
        print(z)
elif y<x and y<z:
    if x>z:
        print(x)
    else:
        print(z)
elif z<x and z<y:
    if x>y:
        print(x)
    else:
        print(y)
