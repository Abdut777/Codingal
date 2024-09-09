numberSmallest = int(input("enter the smallest number:"))
numberLargest = int(input("enter the largest number"))
while numberLargest:
    numberStore = numberLargest
    numberLargest = numberSmallest % numberLargest
    numberSmallest = numberStore

print("LCM is:", numberSmallest)