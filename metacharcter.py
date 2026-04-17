import re
#pattern search using meta characters
#[] will search for meta chars
mytxt="Hello world"
#find all the character from ato m
result=re.findall('[a-m]',mytxt)
print(result)

#\ used to denote special sequence
mytxt="I will give you 564 points"
#find all the digits /decimal chars in the string
result=re.findall('\d',mytxt)
print(result)

#. used to denote any char except new line
#find all substring starts with po and have 3 chars and end with s
result=re.findall('po...s',mytxt)
print(result)

# ^ check if the entire string starts with the substring , works multiline
mytxt="my fav flowers are jasmineflower and sunflower"
#find all substring starting with 'jasmine
result=re.findall('^m',mytxt)
print(result)

# $ to check if the entire string end with the substring
# check if the string ends with "jasmine flower"
result=re.findall('pasminef',mytxt)
print(result) 

#\A used to find if a string is starting with substring 
mytxt="my fav flowers are jasmineflower and sunflower"
result=re.findall('\Ajasmine',mytxt)

#checking using string boundary sequence
#\b to check the string boundary
result=re.findall(r'\ba',mytxt)
print(result)

#check for all substrs ending with 'flower
result=re.findall(r'flower\b',mytxt)
print(result)

#checks for all substrs exactly 'sunflower
result=re.findall(r'\bsunflower\b',mytxt)
print(result)

#Q : write reg expression to find email in a string
mytxt='my mail is mygmail@gmail.com'
myregex=r'\S+@\S+'
result=re.findall(myregex,mytxt)
print(result)