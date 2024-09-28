def myfunction(n):
    for i in range(0,n+1):
        print("first Loop")

j=1
while(j<=n+1):
    print("second Loop",j)
    j=j*2

for i in range(0,100):
    print("third Loop")

print("Function avobe will take time:")
print("0(N)+ 0(log N) + 0(1)")