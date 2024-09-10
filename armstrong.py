number=int(input("Input number:"))
result=0
temp=number%10
while temp!=0:
    digit=temp%10
    result=result+digit**3
    temp=temp//10
print(result)
if number==result:
    print(number,"in an armsdtong number")

else:
    print(number,"is not an armstrong number")