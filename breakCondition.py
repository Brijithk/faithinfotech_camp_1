# for i in range(5):
#     print("*"*i)
# for j in range(5,0):
#     print("*"*j)
# for j in range(5,0,-1):
    # print("*"*j)
#print numbers 1 to 20 using while loop
num=1
while num!=21:
    print(num)
    num+=1
#print all even numbers between 2 to 50
for i in range(2,51,2):
    print(i)
#use a while loop to countfrom 10 to 1 and then print "go"
count=10
while count!=0:
   print(count)
   count=count-1
print("go")
#print all integer multiples of 5 below 100
for i in range(0,100,5):
    print(i)
#from the list, print only even numbers
number=[12,5,21,60,82,78,99,54]
for i in number:
    if i%2==0:
        print(i)