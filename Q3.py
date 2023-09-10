num=int(input("Enter your phone number's total digit count: "))
l1=[]
for i in range(num):
    i=int(input("Enter your phone number one by one digit:"))
    l1.append(i)
print("the number is: ", l1)

l1.sort()
print("After sorting the list with ascending order",l1)