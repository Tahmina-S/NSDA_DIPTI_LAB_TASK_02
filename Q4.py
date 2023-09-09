print("Enter your phone number one by one digit:")
l1=[]
for i in range(11):
    i=int(input())
    l1.append(i)
print("the number is: ", l1)

evenlist=[]
oddlist=[]

for i in l1:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("Evenlist is:",evenlist)
print("Oddlist is:", oddlist)