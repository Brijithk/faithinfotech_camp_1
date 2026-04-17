#1
fruits=['apple','mango','orange','lemon','banana']
print(fruits)
#2
print(fruits[2])
#3
fruits[1]="grapes"
print(fruits)
#4
fruits.append("kiwi")
print(fruits)
#5
fruits.insert(2,"pineapple")
print(fruits)
#6
try:
    fruits.remove("bananna")
    print("banana is removed")
except:
    print("banana is not present previously")
#7
print(fruits[:3])
#8
print("apple" in fruits)
#9
fruits.sort()
print(fruits)
#10
fruits.reverse()
print(fruits)
#11
lang=('python','java','c')
print(lang)
#12
Devices=('laptop','tablet','phone','watch')
print(Devices[1])
#14
print(Devices[-1])
#15
Cities=('mumbai','delhi','chennai')
print('delhi' in Cities)
#17
Sports=('cricket','football','hockey','tennis')
print(len(Sports))
#19
value='Python'
print(value*4)
#20
del value
print(value)