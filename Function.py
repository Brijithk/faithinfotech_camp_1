# 108
#creating a function
# def hello():
#     print("hello world")
# #calling a function
# hello()

# def add_numbers(a,b):
#     return a+b

# result=add_numbers(3,5)
# print(result)

#find area of the rectangle using the function
# def calculate_area(length,width):
#     area=length*width
#     return area
# rectangle_area=calculate_area(5,10)
# print("area of triangle: ",rectangle_area)

#write a function to find the maximum of 2 numbers
# def find_max(a,b):
#     if a>b:
#         return a
#     else:
#        return b
# maximum=find_max(15,7)
# print(maximum)

#write a function to check if it is even or odd
# def evenOrOdd(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# store=evenOrOdd(50)
# print("the entered number is",store)

# 3. Check whether a number is an Armstrong number.
# num=153
# sum=0

# for i in str(num):
#     sum=sum+(int(i)**len(str(num)))
# if(num==sum):
#     print("the entered number is an armstrong number")
# else:
#     print("not armstrong")

# 4. Print all Armstrong numbers between 1 and 1000.
# start=1
# end=1000
# for i in range(start,end):
#     sum=0
#     for j in str(i):
#         sum=sum+(int(j)**len(str(i)))
#     if sum==i:
#         print(i,end=" ")


#5. Generate the Fibonacci series up to n terms without recursion.
# n=int(input("Enter a number\n"))
# a=0

# b=1
# sum=0
# for i in range(1,n+1):
#     sum=a+b
#     a=b
#     b=sum
#     print(sum)

# 6. Print pattern: 1, 22, 333, 4444, 55555.
# n=int(input("Enter a number\n"))
# for i in range(1,n):
#     print(str(i)*i)

# 8. Reverse a number and check if it is a palindrome.
# n=int(input("Enter a number\n"))
# temp=str(n)[::-1]
# if n==int(temp):
#        print("it is palindrome")
# else:
#        print("not palindrome")

# 9. Find the GCD of two numbers using loops.
# a=36
# b=60
# temp=a//2 if b>a else b//2
# print("1 :",temp)
# gcd=a if b>a else b
# print("2 :",gcd)
# for i in range(1,temp):
#     if a%i==0 and b%i==0:
#         gcd=i
# print(gcd)

# a=60
# b=36
# temp=a
# while True:
#     temp=a%b
#     if temp==0:
#         break
#     else:
#         a=b
#         b=a%b

# 1. Student Names List  
 
# • Create a list of 5 student names. 
# • Print the name at a specific index. 
# • Add a new student to the list. 
# • Update the name of a student in the list. 
# • Remove a student from the list. 
# • Loop through the list and print all names.

# list=['jack','john','tom','rom','sam']
# print(list[1])
# list.append('jarry')
# print(list)
# list.remove('jack')
# print(list)
# for i in list:
#     print(i)

# 2. Shopping List  
 
# • Create a list of grocery items. 
# • Add two more items to the list. 
# • Change one item name in the list. 
# • Remove one item from the list. 
# • Print the total number of items in the list. 

list=['carrot','onion']
list.append('beetroot')
list.append('lactusse')
print(list)
