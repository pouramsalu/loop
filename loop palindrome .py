# n=int(input("enter the number"))
# pal=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if pal==rev:
#     print("palindrome number")
# else:
#     print("not palindrome number")

    
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    k=i-1
    while k>=1:
        print(k,end=" ")
        k-=1
    print()
    i+=1


