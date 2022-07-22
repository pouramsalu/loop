# A 
# B C 
# C D E 
# D E F G 
# E F G H I 

n=int(input("enter the number"))
i=0
while i<n:
    k=ord("A")+i
    j=0
    while j<=i:
        print(chr(k),end=" ")
        k+=1
        j+=1
    i+=1
    print()