bs=int(input())
hra= (20/100)*bs
ta=(5/100)*bs
da=(10/100)*bs
gross=bs+hra+ta+da
if gross<300000:
    print("0% income tax")
elif gross>300000 and gross<1000000:
    print("10% income tax")
elif gross>1000000 and gross<2500000:
    print("20% income tax")
elif gross>2500000:
    print("30% income tax")