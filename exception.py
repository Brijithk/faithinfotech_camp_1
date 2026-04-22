# try:
#     #code that might raise an exception
#     number=int(input("enter a number"))
#     result=10/number
# except ValueError:
#     #Handle value error if the user enters a non-numeric value
#     print("Invalid input.please enter a number")

# except ZeroDivisionError:
#     #Handle ZeroDivisionError if the user enters 0
#     print("Cannot divide by zero")

# else:
#     #code to execute if no exception occur
#     print("Result :",result)

# finally:
#     print("end of program")



#login function
# def login():
#     try:
#         #credentials
#         correct_username="admin"
#         correct_password="admin123"

#         #user input
#         username=input("Enter username :")
#         password=input("Enter password:")

#         if username=="" or password=="":
#             raise ValueError("Username or password cannot be empty")
        
#         if username!=correct_username:
#             raise Exception("Invalid username")
        
#         if password!=correct_password:
#             raise Exception("Invalid password")
        
#         print("Login Successful")

#     except ValueError as ve:
#         print("Error :",ve)

#     except Exception as e:
#         print("Login failed :",e)

#     finally:
#         print("End of login process")

# #call function
# login()

#Ask the user to enter marks .
#if marks<0 or >100---------->rase invalid marks
#else print valid marks


try:
    userMarks=int(input("Enter the marks:\n"))

    if userMarks <0 or userMarks > 100:
        raise Exception("Enter a valid mark")
    
except Exception as e:
    print("Error",e)

else:
    print("valid mark")

finally:
    print("---end---")