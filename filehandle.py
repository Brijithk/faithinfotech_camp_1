#file handling
# myfile=open("myfile.txt","r")
# print(myfile.read())

#to return the first 10 characters of the file
# myfile=open("myfile.txt","r")
# print(myfile.read(5))

#update an existing file, add 'a' parameter to the open ()
#'a'-Append - will append to the end of the file
myfile=open("myfile.txt","a")
myfile.write("adding new content added at end of file")
myfile.close()
myfile=open("myfile.txt","r")
print(myfile.read())