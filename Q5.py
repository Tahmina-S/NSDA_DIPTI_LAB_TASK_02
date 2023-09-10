num=int(input("Enter num: "))

"""""
def isPrime(num):
    if num==1:
        print("Not Prime.")
    else:
        count=0
        a=int(num/2)
        for i in range(2,a):
            if num%i==0:
                count=1
        if count==0:
            print("Prime")
        else:
            print("Not Prime")
isPrime(num)
"""

if num==1:
    print("NOT Prime.")
elif num>1:
    flag=False
    for i in range(2,int(num/2)):
        if num%i==0:
            flag=True
    if flag:
            print("Prime")
    else:
            print("NOT Prime.")