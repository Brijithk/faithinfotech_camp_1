# login credentials
# -----------------
correctUserName="Admin"
correctPassword="1234"

#default value:
#------------
# global textId
textId=0
textData={}

def login():
    attempts=3
    while(attempts!=0):
        userName=input("Enter your name :")
        password=input("Enter the password :")
        if userName==correctUserName and password==correctPassword:
            print("login successful")
            print("------------------")
            return True
        else:
            print("Invalid credentials , Please try again !")
            attempts-=1
            print("attempts left :",attempts)

    if attempts==0:
        print("Three wrong attempts.")   
        print("closing the application....") 
        return False
  
def homepage():
    print("welcome to home page")
    print("--------------------")

    while True:
     print("--------------------------------------")
     print("Choose an operation to perform:\n1. Add test\n2. See List of Test\n3. Search and View Test\n4. Go to Main Menu:")
     userChoice=input()
     match userChoice:
          case '1':
            addTest()
            
          case '2':
            #redirect to see list page
            viewAllTest()
            
          case '3':
              #redirect to search test page
              searchTest()
          case '4':
              #redirect to previous page
              print()
              break
          case _:
                print('Wrong choice. Please choose an item from the menu.')
        
def addTest():
    global textId
    global textData
    # print(textId)
    print("---------------------")
    print("Add test")
    print("-------------------")
    testName=input("Enter a test name\n")
    lowRange=int(input("Enter lower Range\n"))
    highRange=int(input("Enter higher range\n"))
    while lowRange>highRange :
        print("Please Enter a valid number ! your low range value is :",lowRange)
        highRange=int(input())
    unit=input("Enter the unit\n")
    price=input("Enter the price\n")
    isDisable=False
    isExist=False
    # if len(textData)!=0:
    #  for i in textData:
    #     print ("---i---:",i)
    #     if (i["testName"]==testName and i["lowRange"]==lowRange and i["highRange"]==highRange
    #         and i["unit"]==unit and i["price"]==price):
    #             isExist=True
    if isExist!=True:
    #   textId+=1
      textData[textId]={
        "testName":testName,
        "lowRange":lowRange,
        "highRange":highRange,
        "unit":unit,
        "price":price,
        "isDisable":isDisable
      }
      textId+=1
      print("Added the text successfully")
    else:
        print("Test already exists")

def viewAllTest():
    print("All available test")
    print("--------------------")
    # for i in textData:
    #     step=1
    #     print("--",step,"--",i["testName"],"--",i["lowRange"],"--",i["highRange"],"--",i["unit"],"--",i["price"])
    #     step+=1
    for testName,lowRange in textData.items():
        step=1
        print("--",testName,"--",lowRange,"--")
    for item in textData:
        print("--",item.get("testName"),"--",item.get("lowRange"))
   

def searchTest():
    print("Search a test")
    print("----------------")
    print("How would you like to search for the test?")
    print("1. By Test code")
    print("2. Go to Manage Test Menu")
    userChoice=int(input())
    if userChoice==1:
        searchedTest=int(input("Enter the test code:\n"))
        if searchedTest in textData:
             foundTest=textData[searchedTest]
             print("Given code Details")
             print("------------------")
             print(foundTest)
             print("testName :",foundTest["testName"])
             print("lowRange :",foundTest["lowRange"])
             print("highRange :",foundTest["highRange"])
             print("unit :",foundTest["unit"])
             print("price :",foundTest["price"])
             print("------------------------------")
             print("How do you like to proceed ?")
             print("1. Edit Test")
             print("2. Disable Test ")
             print("3. Go Back")
             userSelection=input()
             if userSelection=="1":
                 if textData[searchedTest]["isDisable"]==False :
                    print("-----------------------")
                    print("Your old price is",textData[searchedTest]["price"])
                    print("Enter a new price to update:")
                    newPrice=input()
                    textData[searchedTest]["price"]=newPrice
                 else:
                    print("The selected test data is disabled and cannot be modified !")    
             elif userSelection=="2":
                 if textData[searchedTest]["isDisable"]==True :
                    print("The entered test code is already disabled. Do you want to change? (y/n)")
                    userChoice=input()
                    if userChoice=="y":
                        textData[searchedTest]["isDisable"]=False
                        print("Updated successfully")
                    else:
                       print("No changes")
                 else:
                     textData[searchedTest]["isDisable"]=True
                     print("Do you want to disable the Test? (y/n)")
                     userChoice=input()
                     if userChoice=='y':
                        print("The current Test code has been disabled")
                     else:
                         print("No Changes has been made")
                 

        else:
             print("Sorry, there is no such Test.")


# if login():
#     homepage()

homepage()