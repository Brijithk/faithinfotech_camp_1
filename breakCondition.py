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
#from the list add 10 to each
number=[12,5,21,60,82,78,99,54]
for i in number:
    print(i+10)
#4. Given: str = 'PyNaTive' Arrange characters so lowercase letters come first, then uppercase.
str = 'PyNaTive'
lower=""
upper=""
for i in str:
    if i.isupper():
        # print("i.isupper",i.isupper())
        upper=upper+i
        # print("upper",upper)
    elif i.islower :
        lower=lower+i
        # print(lower)
print(lower+upper)
# 5. Given: str = 'P@#yn26at^&i5ve;' Count letters, digits, and special characters.
c_letter=c_digit=c_special=0
str = "P@#yn26at^&i5ve;"
for i in str:
    if i.isdigit():
        c_digit+=1
    elif i.isalpha():
        c_letter+=1
    else :
        c_special+=1
print("letters :",c_letter ,"digits :",c_digit ,"special :",c_special)
# 20. Given: str = '(())()' Check if parentheses are balanced.
# str = '()'
# stack=[]
# for i in str:
#     if i=="(" and len(str)%2!=0:
#         print("length of str is",len(str))
#         print("unbalanced bracket 1")
#         break
#     elif i=="(":
#         stack.insert(len(stack)-1,"(")
#         print("i am here 1")
#     elif i==")" and i==len(str)-1:
#         print("balanced 1")
#     elif i==")":
#         if len(stack)==0:
#             print("balancedn 2")
#             break
#         elif stack[len(stack)-1]=="(":
#             print("->",i.,len(str))
#             stack.pop()
#             print("i am here 2")
#         else :
#             print("unbalanced bracket 2")
#             break
    
    
            
