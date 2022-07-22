

# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# n=int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# i=0
# while i<6:
#     print(' '*(5-i),end=" ")
#     j=0
#     while j-1<i*2:
#         if j+1>i+1:
#             print((i*2)-j+1,end=" ")
#         j+=1
#     print()
#     i+=1




# 5
# 5 4 
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# i=5
# while i>0:
#     j=5
#     while j>=i:
#         print(j,end=" ")
#         j=j-1
#     i=i-1
#     print()


# *
# * *
# * * * 
# * * * *
# * * * * *

# i=1
# while i<=5:
#     print('*'* i)
#     i=i+1


# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# n=int(input("enter the number of rows"))
# for i in range(1,n+1):
#     for j in range (65,65+i):
#         print(chr(j),end=" ")
#     print()


# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(i,end=" ")
#         j+=1
#     i+=1
#     print()

n=5
i=1
while i<=5:
    k=n-i
    j=1
    while j<=5:
        print(chr(k+65),end=" ")
        k+=n
        j+=1
    i=i+1
    print()
    