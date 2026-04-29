# customers={
#     123456789:{
#         "name":"john",
#         "pin":1234,
#         "panNumber":768675687,
#         "phoneNumber":8787877676,
#         "balance":600,
#         "minBalance":500

#     },
#     234123876:{
#         "name":"darvin",
#         "pin":2004,
#         "panNumber":888675687,
#         "phoneNumber":9987877676,
#         "balance":1200,
#         "minBalance":500
#     }
# }
# def login():
#     while True:
#         accNumber=input("Enter your account number :\n")
#         pinNumber=input("Enter your pin number :\n")
#         isValid=True
#         for i in str(accNumber):
#             if i.isalpha()==True:
#                 isValid=False
#             elif i.isnumeric()==False:
#                 isValid=False
#         if accNumber=="" or isValid==False:
#             print("Enter a valid Account Number")
#             continue
#         isValidPassword=True
#         for i in pinNumber:
#             if i.isnumeric()==False:
#                 isValidPassword=False
#         if pinNumber=="" or isValidPassword==False:
#             print("Enter a valid Password")
#             continue
#         if len(accNumber)>9:
#             print("Account Number should not have greater than 9 digits")
#             continue
#         elif len(accNumber)<9:
#             print("Account number should not have less than 9 digits")
#             continue
#         if int(accNumber) not in customers:
#             print("Account number doesnot exist")
#             continue
#         if int(pinNumber)!=customers[int(accNumber)]["pin"]:
#             print("Incorrect pin number")
#             print("if you want to generate new pin type :g")
#             print("if you want to retry login enter : r")
#             userChoice=input()
#             match userChoice:
#                 case "g":
#                     generatePin(int(accNumber))
#                 case "r":
#                     continue
#                 case _:
#                     print("Invalid selection.going to login page...")
#                     continue
#         return int(accNumber)
        

# def generatePin(accNumber):
#     userNumber=input("Enter your phone number")
#     if userNumber==str(customers[accNumber]["phoneNumber"]):
#         pin1=input("Enter your new pin")
#         pin2=input("Re-Enter your new pin")
#         if(pin1!=pin2):
#             print("pin doesnot match")
#             generatePin(accNumber)
#         elif len(pin1)!=4 or len(pin2)!=4:
#             print("pin must have 4 digits") 
#             generatePin(accNumber)
#         customers[accNumber]["pin"]=pin1
#     else:
#         print("Phone number doesnot match")
#         generatePin(accNumber)

# def homePage(currentUser):
#     while True:
#         print("Enter the operation to be performed:\n1.Deposit Money\n2.withdrawl money" \
#         "\n3.Show Balance\n4.Transfer Money\n5.Exit")
#         userSelection=input()
#         if userSelection=="1":
#             depositMoney(currentUser)
#         elif userSelection=="2":
#             withdrawMoney(currentUser)
#         elif userSelection=="3":
#             showBalance(currentUser)
#         elif userSelection=="4":
#             transferMoney(currentUser)
#         elif userSelection=="5":
#             print("Thank You")
#             return False
#         else:
#             print("Invalid selection! Try again")

# def depositMoney(currentUser):
#     try:
#         global customers
#         senderAcc=int(input("Enter Account Number to deposit the money :\n"))
#         if senderAcc not in customers:
#             print("The entered Accoun Number doesnot exist")
#             depositMoney(currentUser)
#         depositAmount=int(input("Enter the deposit Money :\n"))
#         if depositAmount<1:
#             print("Enter a number greater than 0")
#             depositMoney(currentUser)
#         tempAmount=customers[currentUser]["balance"]+depositAmount
#         if tempAmount>50000:
#             userPan=int(input("Enter your pan Number to continue :\n"))
#             if userPan!=customers[currentUser]["panNumber"]:
#                 print("The pan Number doesnot match")
#                 depositMoney(currentUser)
#         customers[currentUser]["balance"]=tempAmount
#         print("Amount has been deposited successfully")
#     except:
#         print("Something gone wrong")

# def withdrawMoney(currentUser):
#     try:
#         global customers
#         Acc=int(input("Enter the account number to withdraw the money :\n"))
#         if Acc not in customers:
#             print("The entered account number doesnot exist")
#             withdrawMoney(currentUser)
#         withdraw=int(input("Enter the amount of money to be withdrawn :\n"))
#         availableBalance=customers[currentUser]['balance']-customers[currentUser]['minBalance']
#         if withdraw>availableBalance:
#             print("Insufficient Funds...!!!")
#             withdrawMoney(currentUser)
#         if withdraw>50000:
#             pan=int(input("Enter your pan Number to proceed withdrawl:\n"))
#             if pan!=customers[currentUser]["panNumber"]:
#                 print("The pan number doesnot match")
#                 withdrawMoney(currentUser)
#         customers[currentUser]["balance"]=customers[currentUser]['balance']-withdraw
#         print("Anount has been withdrawl successfully")
#     except:
#         print("somethin gone wrong...")

# def showBalance(currentUser):
#     try:
#         acc=int(input("Enter the account number"))
#         if acc not in customers:
#             print("The entered account number doesnot exist")
#             showBalance(currentUser)
#         print("Your current Balance is",customers[currentUser]["balance"])
#     except:
#         print("Something gone wrong!")

# def transferMoney(currentUser):
#     try:
#         global customers
#         fromAcc=int(input("Enter senders account Number"))
#         toAcc=int(input("Enter the receievers Account Number"))
#         if fromAcc not in customers:
#             print("The senders account number doesnot exist")
#             transferMoney(currentUser)
#         if toAcc not in customers:
#             print("The receivers account number doesnot exist")
#             transferMoney(currentUser)
#         Amount=int(input("Enter the amount you want to transfer :\n"))
#         if Amount>(customers[currentUser]["balance"]-customers[currentUser]["minBalance"]):
#             print("Insufficient Funds")
#             transferMoney(currentUser)
#         customers[currentUser]["balance"]=customers[currentUser]["balance"]-Amount
#         customers[toAcc]["balance"]=customers[toAcc]["balance"]-Amount  
#         print("Transferred amount sucessfully!")  
#     except:
#         print("something gone wrong")    


# store=login()
# homePage(store)

str="https://google.com"
x=str.removeprefix("https://")
print(x.upper())
    