from math import sqrt
x=int(input("Enter your number::"))
for i in range(2,int(sqrt(x))+1):
    
    if x%i==0:
        print("number in not a prime")
        break

else:
    print("number is a prime")