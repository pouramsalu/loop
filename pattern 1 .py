# E J O T Y 
# D I N S X 
# C H M R W 
# B G L Q V 
# A F K P U 

n=5
i=1
while i<=5:
    k=n-i
    j=1
    while j<=5:
        print(chr(k+65),end=" ")
        k+=n
        j+=1
    i+=1
    print()