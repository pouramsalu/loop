#       1
#     2 2
#   3 3 3
# 4 4 4 4

i=1
while i<=5:
    j=5
    while j>=i:
        print(" ",end=" ")
        j-=1
    a=1
    while a<=j:
        print(j,end=" ")
        a+=1
    print()
    i+=1
