def min(l1):
    min=l1[0]
    for n in l1:
        if n<min:
            min=n
    print("So, min num in the list is ", min)

def max(l1):
    max=l1[0]
    for n in l1:
        if n>max:
            max=n
    print("So, max num in the list is ", max)


print("Enter your phone number one by one digit:")
l1=[]
for i in range(11):
    i=int(input())
    l1.append(i)
print("the number is: ", l1)

min(l1)
max(l1)