# #Dictionary -  collection data types with key values
# mystudents={'Tom':5,'Jerry':3,'mickey':4}
# #the keys should be unique , values can have duplicates
# #no access with index numbers

# #access element using keys instead of index
# print(mystudents['Jerry'])
# #dictionary is mutable, we can add or delete items
# mystudents['jerry']=7
# print(mystudents)
# #get() will get the value of the given key
# print(mystudents.get('jerry'))
# #get the list of all keys in the dictionary
# print(mystudents.keys())
# #get the list of all values in the dictionary
# print(mystudents.values())
# #get the list of all items
# print(mystudents.items())
# #to check if an key is there in the dictionary
# print('Tom' in mystudents)
# #to check if an value is there in the dictionary
# print(30 in mystudents.values())
# #update a dictionary with another dictionary
# mystudents2={'superman':20,'ironman':35}
# mystudents.update(mystudents2)
# print(mystudents)
# #delete a specific key value pair
# mystudents.pop('mickey')
# #will remove superman key and its value
# mystudents.clear()
# #clears the dictionary
# print(mystudents)#{}


# #use del operator to delete the entire dictionary
# del mystudents

#LIBRARY MANAGEMENT SYSTEM USING DICTIONARY AND FUNCTIONS
#---------------------------------------------------------

#sample login credentials
userName="admin"
passWord="1234"

#DICTIONARY TO STORE BOOKS
#book_id:{"title":---,"author":---,"price":---}
library={}


#=========================
#login functiom
#========================

def login():
    print("----------------------------------")
    username=input("Enter username")
    password=input("Enter password")
    if username==userName and password==passWord:
        print("Login successful")
        return True
    else:
        print("invalid credentials")
        return False


#---------------------  
#Add book
#-----------------------
def add_book():
    book_id=input("Enter book id:")
    if book_id in library:
        print("Book id already exists ...")
        #it prevents the program from continuing and adding  the book  again
        return
    title=input("Enter book title:")
    author=input("Enter author name:")
    price=float(input("Enter price..."))

    library[book_id]={
        "title":title,
        "author":author,
        "price":price
    }
print("Book added successfully")

#---------------------
#Edit book
#--------------------

def edit_book():
    book_id=input("Enter book id to edit")
    if book_id not in library:
        print("Book not found")
        return
    print("leave blank to keep old value")

    title=input("enter new title")
    author=input("enter author")
    price=input("enter price")

    if title:
        library[book_id]["title"]=title
    if author:
        library[book_id]["author"]=author
    if price:
        library[book_id]["price"]=float(price)

    print("Book updated successfully!\n")

#-----------------------
#list all books
#------------------------
def list_books():
    if not library:
        print("No books available\n")
        return
    print("--------------------")
    for book_id,details in library.items():
        print("Book ID",book_id)
        print("Title:",details["title"])
        print("Author",details["author"])
        print("price",details["price"])
        print("------------------------")
    print()

#-----------------------------
#Search Book
#-----------------------------

def search_book():
    book_id=int(input("Enter book id to search: "))
    if book_id in library:
        details=library[book_id]
        print("Book Found!")
        print("Title",details["title"])
        print("Author",details["author"])
        print("Price",details["price"])
    else:
        print("Book not found")
    print()

#----------------
#delete book
#--------------

def delete_book():
    book_id=int(input("Enter book id to delete:"))

    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!")
    else:
        print("Book not found!")
    print()

#--------------------------------
#Menu Function
#-------------------------------

def menu():
    while True:
        print("-------Menu------")
        print("1.Add Book")
        print("2.Edit Book")
        print("3.list Book")
        print("4.search Book")
        print("5.delete Book")
        print("6.Exit")

        choice=input("Enter your choice from 1 to 6 :")
        if choice=="1":
            add_book()
        elif choice=="2":
            edit_book()
        elif choice=="3":
            list_books()
        elif choice=="4":
            search_book
        elif choice=="5":
            delete_book
        elif choice=="6":
            print("exiting program...")
            break
        else:
            print("Invalid choice")


#--------------------------------
#Main program
#--------------


if login():
    menu()
