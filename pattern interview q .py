# A B C D E 
# B C D E F 
# C D E F H 
# D E F G H 
# E F G H I 

i=0
while i<5:
    k=ord("A")+i
    j=0
    while j<5:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    i=i+1
    print()
    