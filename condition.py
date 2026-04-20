print('my height is 5\' 5" ')
#control flow statements - used to alter default flow og prgm
#conditional statement- control flow based on condition
#if condition
user_input=input("Enter a number 1 or 2:")
if user_input=='1':
    print("you enterd one")
    print("thank you")
elif user_input=='2':
    print("you entered 2")
    print("thank you")
else:
    print("you entered something else")

#converting to a single line if statement
print("you entered 1" if user_input=="1" else "you entered 2")


#converting to a match case statement
#enclosing matchcase inside a function
def number_game(user_input):
    match user_input:
        case "1":
            return "you entered one"
        case "2":
            return "you entered 2"
        case _:
            return "you entered wrong"
#calling the function
print(number_game(user_input))

#Assignment on match case
dob_month=int(input("Enter the month (in number) you born to show your personality \n"))
match dob_month:
    case 1:
        print("your stone is Garnet")
        print("People born in jan are alert")
    case 2:
        print("your stone is Amethyst")
        print("People born in feb are lucky")
    case 3:
        print("your stone is Aquamarine")
        print("People born in mar are naughty")
    case _:
        print("invalid month entered")
