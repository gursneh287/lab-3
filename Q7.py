print("Enter Complex Number 1 (as a+ib): ")
a = float(input("Enter Real Term(a) : "))
b = float(input("Enter Imaginary Term(b) : "))

print("Enter Complex Number 2 (as x+iy): ")
x = float(input("Enter Real Term(x) : "))
y = float(input("Enter Imaginary Term(y) : "))

sum_re = (a+x) 
sum_img = (b+y)
sum_img_print = str(sum_img)+'i'

print("The sum of complex numbers is :", sum_re ,'+',sum_img_print)

product_re = (a*x-b*y)
product_img = (a*y+b*x)
product_img_print = str(product_img)+'i'
print("The product of complex numbers is :",product_re,'+',product_img_print )
