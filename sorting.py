num=[12,11,76,89,5,6]
x=num[0]
for i in range(1,len(num)):
    for j in range(i,len(num)):
        if(x > num[j]):
            x=num[j]
            temp=num[j]
            num[j]=num[i]
            num[i]=temp
            x=num[i]
print(num)
n = 5

for i in range(n):
    num = 3
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()