def min(myNumber):
    min=myNumber[0]
    for n in myNumber:
        if n<min:
            min=n
    print("So, min num in the list is ", min)
    
def max(myNumber):
    max=myNumber[0]
    for n in myNumber:
        if n>max:
            max=n
    print("So, max num in the list is ", max)

digit=int(input("Enter your phone number's digit count limit:"))
myNumber=[]
for i in range(digit):
    i=int(input("Enter {} digit : ".format(i+1)))
    myNumber.append(i)
print("Phone Number is: ",myNumber )

min(myNumber)
max(myNumber)