#        *
#      * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

# n=int(input("enter the number"))
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

i=1
sum=0
while i<=4:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum=sum+1
        j=j+1
    print()
    i=i+1