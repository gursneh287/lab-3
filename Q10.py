x,y,z=map(int,input().split())
if x<y or x<z:
    if y>z:
        print(y)
    else:
        print(z)
elif y<x or y<z:
    if x>z:
        print(x)
    else:
        print(z)
elif z<x or z<y:
    if x>y:
        print(x)
    else:
        print(y)