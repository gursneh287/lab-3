#let a, b, c be sides of triangle
def triangle(a,b,c):
    if (a+b>c and b+c>a and c+a>b):
        print("triangle can be formed")
    else:
        print("triangle can not be formed")
    