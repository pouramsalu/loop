# E D C B A
# * E D C B 
# * * E D C 
# * * * E D 
# * * * * E

i=64
while i<69:
    j=64
    while j<i:
        print("*",end=" ")
        j+=1
    k=69
    while k>i:
        print(chr(k),end=" ")
        k-=1
    i+=1
    print()