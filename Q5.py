num=int(input("Enter num: "))

def isPrime(num):
    count=0
    a=int(num/2)
    # if num==1:
    #     print("Not Sure is prime or not")
    for i in range(2,a):
        if num%i==0:
            count=1
    if count==0:
        print("Prime")
    else:
        print("Not Prime")

isPrime(num)