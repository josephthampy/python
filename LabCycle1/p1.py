a=int(input("Enter current Year"))
b=int(input("Enter final Year"))
print("leap Years Are :")
for i in range (a,b):
    if(i%4==0)and(i%100!=0)or(i%400==0):
        print(i)

