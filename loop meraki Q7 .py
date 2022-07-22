# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
# a=int(input("enter the number"))
# i=a
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     i=i-1
#     print()

# n=int(input("enter the number"))
# i=n
# while i>=1:
#     j=1
#     while j<=n:
#         print(i,end=" ")
#         j=j+1
#     i=i-1
#     print()


# 1 
# B B 
# 3 3 3 
# D D D D 
# 5 5 5 5 5 

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(chr(64+i),end=" ")
#         else:
#             print(i,end=" ")
#         j+=1
#     print()
#     i+=1

# 1
# B B 
# 1 2 3
# D D D D 
# 1 2 3 4 5

i=1
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print(chr(64+i),end=" ")
        else:
            print(j,end=" ")
        j+=1
    print()
    i+=1