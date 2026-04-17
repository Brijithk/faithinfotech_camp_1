#collection datatypes in python
#Lists
studDetails=['Abi',899452,'tvm',50,70,80]
print(studDetails)
print(studDetails[1])
print(studDetails[-1])
print(studDetails[1:5])
print(studDetails[::3])

studDetails.append('KTU')
print(studDetails)

additionalDetails=['CET','KERLA']
studDetails.append(additionalDetails)
print(studDetails)

#extend functiion to extend one list with another list
additionalDetails=['CET','KERLA']
studDetails.extend(additionalDetails)
print(studDetails)

del studDetails[7]
print(studDetails)

#to reverse the list using reverse function
studDetails.reverse()
print(studDetails)

#mixed datatypes list is not allowed
additionalDetails=['ZET','CET','KERLA']
additionalDetails.sort()
print(additionalDetails)

#sort hte list using sorted().Not destructive
#returns back the sorted list.we can save it
additionalDetails=['ZET','CET','KERLA']
mynewlist=sorted(additionalDetails)
print(mynewlist)

#to concatenate use + operator
mynewlist1=[10,20]
mynewlist2=[50,60]
print(mynewlist1+mynewlist2)

#to duplicate use * operator
print(mynewlist2*3)

#use in operator to checkif an item is present
print(50 in mynewlist2) #returns true or false