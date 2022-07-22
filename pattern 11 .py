# E D C B A
# E D C B
# E D C
# E D 
# E

n=int(input("enter the number"))
i=n
while i>=1:
    k=ord("E")
    j=0
    while j<i:
        print(chr(k),end=" ")
        k-=1
        j+=1
    i-=1
    print()