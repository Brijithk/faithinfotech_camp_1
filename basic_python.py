# mystring='A single line string'
# mystring2="This is a single line string"
#for multiline strings use triple quotes
#also called docstring
#it will preserve the single quote as it is
# mystring3='''This  is a multiline
# string'''
# print(mystring3)

#string formatting used to insert variables inside a string
#Mathod 1- using concatenation (error prone and not standard way)
country_name="India"
# print(country_name+" is my country")
# print("All "+country_name+"n's are my brothers and sisters")

#Method 2 - using f for string formatting
print(f"{country_name} is my country")
print(f"All {country_name}ns are my bros")

#Method 3- using % operator for string formatting
computer_make="Lenova"
dollar_rate=95888.52
mytext='The price for this %s computer is ' \
'%d and the exchange rate is %4.2f' %(computer_make,255,dollar_rate)
print(mytext)

#Method 4- using format() method for string formaatting
#here we can refer to the position using index number
computer_make="Lenova"
dollar_rate=95888.52
price=250
name="abhi"
mytext='Hello {3:s} The price for this {0:s} computer is ' \
'{1:d} and exchange' \
'rate is {2:4.2f}'.format(computer_make,price,dollar_rate,name)
print(mytext)
#count function to count the number of substrings in a main string
mystring="tom an jerry went to the park.tom sat down.tom died"
#count no of occurence of "tom" from the 14 th index till 34th index
print(mystring.count('tom',14,34))

#using find() to get the index of first occurecnce of substring.will return -1 if not found
tom_location=mystring.find('jerryu')
print(tom_location)

#index() will return a value error if the substring is not found
jerry_location=mystring.index("tom")
print(jerry_location)

#endswith() fn to check if a string ends with the give substring.if yes return tru else false

print('superman'.endswith('myan'))
print('superman'.endswith('man',3))#true
print('superman'.endswith('man',3,6))#false


#isalpha() to check if string contains only alphabets
print('super'.isalpha())

#isdigit() to check if string contains only numbers
print("123".isdigit())

#isalphanum() to check if string contains only alphabet and numbers
print('123'.isalnum())#true
print(' 1 2 3 '.isalnum())#false

#isupper() to check for uppercase , islower() to check lowercase
#istitle() for titlecase
print("HELLO".isupper())
print("HELLO".islower())
print("HELLO".istitle())
print("HELLO".upper())
print("HELLO".lower())

#in python we donot have array
#join() to join chars n tuple using the seperator provided
mytuple=('hello','world','how','are','you')
seperator="**"
print(seperator.join(mytuple))

#replace() to replae s substring with another substring
print('Hello world'.replace('Hello','Hi'))

#Using Regular Expression Module
#findall() function returns a list of all matches
import re
txt='cat and mouse had a race.cat ate mouse.end of mouse'
occurances=re.findall("mouse",txt)
print(occurances)

#search() will return back an object
# occurances obj contains span(), the string , the group()
print(occurances.span())#(8,13)-start and end of its 1st occurance
print(occurances.string)#return the original string
print(occurances.group())#return back the pattern that we are 

#3.split() will split the string at the occurance of match
#return back a list with splitted string
splitted_list=re.split("mouse",txt)
print(splitted_list)

#4,sub() will replace/subtitute a substring with another
subs_string=re.sub("cat","dog",txt)
print(subs_string)
#dog and mouse had a race.dog ate mouse.end of mouse