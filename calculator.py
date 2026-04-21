# inp=input("enter the exp")
# print(eval(inp))
user_choice=-1
def getChoice():
    user_choice=int(input("choose a opertion to perform:\n1.addition\n2.subtraction\n3.multiplication\n4.division\n"))
    return user_choice
user_choice=getChoice()
while user_choice!=5:
    match user_choice:
        case 1:
            a=int(input("enter the first input:\n"))
            b=int(input("enter the second input:\n"))
            print("Adiiton :",a+b)
            getChoice()
            break
        case 2:
            a=int(input("enter the first input:\n"))
            b=int(input("enter the second input:\n"))
            print("Subtraction :",a-b)
            getChoice()
            break
        case 3:
            a=int(input("enter the first input:\n"))
            b=int(input("enter the second input:\n"))
            print("Multiplication :",a*b)   
            getChoice()
            break        
        case 4:
            a=int(input("enter the first input:\n"))
            b=int(input("enter the second input:\n"))
            print("Division :",a/b) 
            getChoice()
            break 
        case 5:
            print("Closing...") 
            break
        case _:
            print("This is a default condition")