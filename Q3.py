#let a, b, c be sides of triangle
a = int(input('enter side a: '))
b = int(input('enter side b: '))
c = int(input('enter side c: '))
if (a+b>c and b+c>a and c+a>b):
    print("triangle can be formed")
else:
    print("triangle can not be formed")
    
