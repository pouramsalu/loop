# 5 5 5 5 5 
#   * * * *
#     3 3 3 
#       * *
#         1

n=int(input("enter the number"))
i=n
while i>0:
    j=n
    while j>0:
        if i>=j:
            if i%2==0:
                print("*",end=" ")
            else:
                print(i,end=" ")
        else:
            print(" ",end=" ")
        j-=1
    i-=1
    print()