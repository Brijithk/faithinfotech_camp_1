#1 Write a program to check whether a number is positive.

getNumber=int(input("Enter a number:\n"))
print("Positive" if getNumber>0 else "Negative" )

#2 Write a program to check whether a number is divisible by 5

getNumber=int(input("Enter a number:\n"))
print("divisible by 5" if getNumber%5==0 else "Not divisible by 5" )

# Write a program to check if a person is eligible to vote (age ≥ 18).

getNumber=int(input("Enter a number:\n"))
print("eligible to vote" if getNumber>=18 else "Not eligible to vote" )

# Write a program to check whether a number is a multiple of 3.

getNumber=int(input("Enter a number:\n"))
print("divisible by 3" if getNumber%3==0 else "Not divisible by 3" )

# Write a program that checks if the entered password equals `"python123"`.

getPassword=input("Enter a Password:\n")
print("password matched" if getPassword=="python123" else "password not matched" )

# Write a program to check whether a number is even or odd.

getNumber=int(input("Enter a number:\n"))
print("even" if getNumber%2==0 else "odd" )

# Write a program to find the largest of two numbers.

getA=int(input("Enter a number for a:\n"))
getB=int(input("Enter a number for b:\n"))
print("a is greater" if getA>getB else "b is greater" )

# If marks ≥ 40 → Pass
# Else → Fail

getMarks=int(input("Enter the mark\n"))
print("pass" if getMarks>=40 else "fail")

# If temperature > 30 → Print "Hot"
# Else → Print "Normal"

getTemp=int(input("Enter the temperature\n"))
print("Hot" if getTemp>30 else "Normal")

# 10. Grade Calculator
# Marks → Grade
# * 90+ → A
# * 75–89 → B
# * 50–74 → C
# * Below 50 → Fail

getMarks=int(input("Enter the mark\n"))
if(getMarks>89):
    print("Grade : A")
elif(getMarks>74):
    print("Grade : B")
elif(getMarks>49):
    print("Grade : C")
else:
    print("Fail")

# 11. Calculator Program

# Take two numbers and an operator (`+`, `-`, `*`, `/`).
# Perform the operation using `if-elif-else`.

getA=int(input("Enter the first Number:\n"))
getB=int(input("Enter the second Number:\n"))
getSymbol=input("Enter a symbol to perform the operation like: + - * /")
if getSymbol=="+":
    print("Addition :",getA+getB)
elif getSymbol=="-":
    print("Subtraction :",getA-getB)
elif getSymbol=="*":
    print("Subtraction :",getA*getB)
else:
    print("Division :",getA/getB)

# 12. Day of the Week

# Input a number (1–7) and print the corresponding day.

getInput=int(input("Enter a number between 1 to 7"))
week=['sunday','Monday','tuesday','wednesday','thursday','friday','saturday']
print("the number you entered represent the day",week[getInput-1])

# 13. Income Tax Calculator
# Based on income:
# * ≤ 2,50,000 → No tax
# * ≤ 5,00,000 → 5%
# * ≤ 10,00,000 → 20%
# * Above → 30%

userIncome=int(input("Enter your income"))
def getTax(amount):
    if amount <= 250000:
        return amount*0
    elif amount <=500000:
        return amount*0.05
    elif amount <=1000000:
        return amount*0.20
    else:
        return amount*0.30
print("The tax amount for your account is : ",getTax(userIncome))

# 14. Age and License Check
# If age ≥ 18 AND has license → Can drive
# Else → Cannot drive

getAge=int(input("Enter your age : "))
getLicense=input("say you have license or not : y / n")
if(getAge>=18 and getLicense=="y"):
    print("you can drive")
else:
    print("not allowed to drive")

# 15. Scholarship Eligibility
# If marks ≥ 80 AND attendance ≥ 75% → Eligible

getMarks=int(input("Enter your marks:\n"))
getAttendance=int(input("Enter your attendance %"))
if getMarks>=80 and getAttendance>=75:
    print("You are eligible for scholarship")
else:
    print("You are not eligible for scholarship")

# 16. Number Range Check
# Check whether a number lies between 10 and 50

getNumber=int(input("Enterf a number"))
print("It lies below 50" if getNumber<50 else "it lies after 50")

# 17. Electricity Bill
# Units consumed:
# * ≤100 → ₹5/unit
# * ≤200 → ₹7/unit
# * > 200 → ₹10/unit
# Calculate total bill.

getUnits=int(input("Enter the number of unit you have consumed"))
if getUnits<=100:
    print("Total bill",5*getUnits)
elif getUnits<=200:
    print("Total bill",7*getUnits)
else:
    print("Total bill",10*getUnits)

# 18. Login System
# Check username and password:
# * Both correct → Login successful
# * Username correct but wrong password → Incorrect password
# * Otherwise → User not found

getUsername=input("Enter a username")
getPassword=input("Enter a password")
if(getUsername=="admin" and getPassword=="1234"):
    print("Login Successful")
elif getUsername=="admin":
    print("User not found")
else:
   print("Incorrect password") 

