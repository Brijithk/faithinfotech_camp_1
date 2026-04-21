#1
# password="password123"
# retry=True
# while retry:
#     userPassword=input("Enter the password\n")
#     if(userPassword==password):
#         print("Password is correct")
#         retry=False
#     else:
#         print("Try Again")
#2
# secretNumber=9
# retry=True
# while retry:
#     userGuess=int(input("Enter a number\n"))
#     if(userGuess==secretNumber):
#         print("Guess is correct")
#         retry=False
#     else:
#         print("Try Again")
#3
# for i in "banana":
#     print(i)
#4
# a="apple"
# b="banana"
# a,b=b,a
# print("a is ",a, "b is ",b)
#5
# while True:
#     checkPrime=int(input("Enter a number\n"))
#     isPrime=True
#     n=checkPrime-1
#     while n>1:
#         if checkPrime%n==0:
#             isPrime=False
#             # print("checkPrime%n",checkPrime%n)
#             break
#         else:
#             n-=1
#             # print("else 1")
#     if isPrime==True:
#         print("the entered number is a prime")
#         break
#     else:
#         print("it is not a prime")
#6
# lst=[1,2,3,4,5]
# print(lst[len(lst)//2])
#Python program to check leap year
# while True:
#     inp=int(input("Enter a year"))
#     if inp%4==0:
#         print("it is leap year")
#     else:
#         print("not leap year")
# lst=["all","and","are","ape"]
# temp=[]
# for i in lst:
    # if 'e' in i:
    #     temp.append(i)
# temp=[i for i in lst if 'e' in i]
# print(temp)
# temp=["hello" for i in lst]
# temp=[i.upper() for i in lst]
# temp=[i for i in lst if i==all ]
# print(temp)
# low=int(input("enter lowest year"))
# high=int(input("enter highest year"))
# years=list(range(low,high+1))
# leap_years=[i for i in years if (i%4==0 and i%100!=0) or (i%400==0)]
# print(len(leap_years))
# high=int(input("enter highest year"))
# for i in range(high):
#     print("*"*i)
# 1. Print all prime numbers between 1 and n (user input).
n=int(input("enter hte ending number"))
for i in range(3,n+1):
    isPrime=True
    for j in range (2,(i//2)+1):  
        if i%j==0:
            isPrime=False
            break
    if isPrime==True:
        print(i," ")