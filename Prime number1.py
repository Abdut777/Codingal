x=int(input ("Enter yoour number:"))
for i in range(2,x-1):
 
 if x%i==0:
  print("number is not prime")
  break

else:
  print("number is a prime number")

