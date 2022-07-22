# 1
# A B 
# 1 2 3 
# A B C D 
# 1 2 3 4 5 
# A B C D E F 

i=1
while i<=6:
    j=1
    k=ord("A")
    while j<=i:
        if i%2!=0:
            print(j,end=" ")
        else:
            print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1