


# n=int(input("enter the number"))
# i=5
# while i>=1:
#     j=1
#     while j<=n-1:
#         print("*",end=" ")
#         j+=1
#     j=0
#     while j<i:
#         print(chr(64+i),end=" ")
#         j+=1
#     i-=1
#     print()

# E D C B A
# * E D C B 
# * * E D C 
# * * * E D 
# * * * * E
# i=64
# while i<69:
#     j=64
#     while j<i:
#         print("*",end=" ")
#         j+=1
#     k=69
#     while k>i:
#         print(chr(k),end=" ")
#         k-=1
#     i+=1
#     print()


i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1

