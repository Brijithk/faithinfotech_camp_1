# 3. Exam Marks  
 
# • Create a list of marks scored in 5 subjects. 
# • Print the marks of a specific subject. 
# • Update a mark for one subject. 
# • Add marks of one more subject. 
# • Find and print the highest and lowest marks. 

list=[56,76,87,34,23]
print(list[len(list)//2])
list[0]=0
print(list)
list.append(99)
print(list)
max=min=list[0]
for i in list:
    if i > max:
        max=i
    elif i<min:
        min=i
print(max,min)