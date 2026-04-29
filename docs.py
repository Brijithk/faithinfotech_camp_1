# 3. Exam Marks  
 
# • Create a list of marks scored in 5 subjects. 
# • Print the marks of a specific subject. 
# • Update a mark for one subject. 
# • Add marks of one more subject. 
# • Find and print the highest and lowest marks. 

# list=[56,76,87,34,23]
# print(list[len(list)//2])
# list[0]=0
# print(list)
# list.append(99)
# print(list)
# max=min=list[0]
# for i in list:
#     if i > max:
#         max=i
#     elif i<min:
#         min=i
# print(max,min)

# 4. Favourite Movies  
 
# • Create a list of your top 5 favourite movies. 
# • Print the first and last movie from the list. 
# • Replace one movie with a new one. 
# • Sort the list in alphabetical order. 
# • Reverse the order of the list. 

# list=["harry","12th","alapuzha","padaikalam","premalu"]
# print(list)
# print(list[0],list[-1])
# list[0]="tom"
# print(list)
# list.sort()
# print(list)
# print(list[::-1])

# 5. Travel Destinations  
 
# • Create a list of 5 places you want to visit. 
# • Add a new destination to the list. 
# • Change one of the destinations. 
# • Remove a destination from the list. 
# • Print all destinations using a loop.

# list=["kerla","goa","london","france","usa"]
# print(list)
# list.append("australia")
# print(list)
# list[0]="china"
# print(list)
# list.pop()
# print(list)
# for i in list:
#     print(i)

 
# 6. Days of the Week  
 
# • Create a tuple with names of the 7 days. 
# • Print the day at index 2. 
# • Check if 'Sunday' exists in the tuple. 
# • Find the index of 'Friday'. 
# • Count how many times 'Monday' appears in the tuple. 

# tuple=("mon","tue","wed","thur","fri","sat","sun")
# print(tuple[2])
# print("sun" in tuple)
# print(tuple.index("fri"))
# print(tuple.count("mon"))

# 7. Coordinates  
 
# • Create a tuple with x and y coordinates. 
# • Print the x coordinate. 
# • Unpack the tuple into two variables. 
# • Create a nested tuple with 3 coordinate pairs. 
# • Access the y coordinate of the second pair. 

# t=([1,2],[2,3])
# print(t)
# print([i[0] for i in t])
# ty=((1,2,3),(4,5,6))
# print(ty[1][1])

# 8. Colours  
 
# • Create a tuple with 5 colour names. 
# • Check if a specific colour exists in the tuple. 
# • Print the length of the tuple. 
# • Join two tuples together. 
# • Repeat the tuple twice and print it. 

# color=("yellow","pink","red","black","white")
# print("blue" in color)
# print(len(color))
# colors=("orange","violet")
# print(color+colors)
# print(color*2)

# 9. Fruits Basket  
 
# • Create a tuple of fruit names.Print the fruit at index 3. 
# • Find the index of a specific fruit. 
# • Count how many times a fruit appears. 
# • Convert the tuple to a list and add a new fruit. 

# tuple1=("orange","apple","grapes","pineapple","guova")
# print(tuple1[0])
# print(tuple1.count("orange"))
# a=list(tuple1)
# a.append("dates")
# print(a)

# 10. Student Info  
 
# • Create a tuple with student name, age, and grade. 
# • Unpack the tuple into three variables. 
# • Print the student’s name using unpacked variables. 
# • Check if a specific grade exists in the tuple. 
# • Find the length of the tuple.

# ---easy---


# 1. School Marks Tracker  
 
# • Create a dictionary to store marks for 5 subjects (e.g., Math, Science, English, 
# History, Computer). 
# • Print the marks of a specific subject. 
# • Add a new subject with marks. 
# • Update the marks of one subject. 
# • Remove a subject from the dictionary. 
# • Loop through the dictionary and print all subjects with their marks.

# marks={"math":78,"science":33,"english":98,"history"=-9
