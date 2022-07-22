# A
# 2 2
# A B C
# 4 4 4 4
# A B C D E

i=1
while i<=5:
    j=1
    k=ord("A")
    while j<=i:
         if i%2==0:
            print(i,end=" ")
         else:
             print(chr(k),end=" ")
         j=j+1
         k=k+1
    print()
    i=i+1