n = int(input("Enter a 3 digit number :"))
x = n//100
y = (n-(x*100))//10
z = (n-(x*100)-(y*10))
sum=(x+y+z)
print(sum)
if sum%3==0:
    print("sum is divisible by 3")
else:
    print("sum is not divisible by 3")