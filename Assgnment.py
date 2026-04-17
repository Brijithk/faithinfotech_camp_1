#1
str='Python'
length=len(str)
newStr=str[0]+str[int(length/2)]+str[length-1]
print(newStr)
#2
str='JhonDipPeta'
length=len(str)
newStr=str[int(((length)/2)-1):int(((length)/2)+2)]
#mid=len(str)//2
# mid-1:mid+2
print(newStr)
#3
s1='Ault'
s2='Kelly'
length=len(s1)
newStr=s1[0:int(length/2)]+s2+s1[int(length/2):length]
print(newStr)
#4,5,6-not needed
#7
str='12345'
print(str.isdigit())
#8
import re
str='Emma is good developer.Emma is a writer'
occurance=re.findall("Emma",str)
print(occurance)
#9
s1='Yn'
s2='PYnative'
print(s2.index(s1))
#10    - not completed  
s = "Emma is a data scientist who knows Python. Emma works at google."
pos = s.rfind("Emma")
print("Last position:", pos)
#11
s = 'ABCDEFGHI'
part_length = len(s) // 3
part1 = s[0:part_length]
part2 = s[part_length:2*part_length]
part3 = s[2*part_length:]
print(part1, part2, part3)
#12
str = 'madam'
revStr=str[::-1]
print(revStr==str)
#13
str = "Welcome to USA. usa awesome, isn't it?"
newStr=str.upper()
print(newStr.count("USA"))
#14
str = 'PYnative'
print(str[::-1])
#15
s = "Emma is a data scientist who knows Python. Emma works at google."
index = s.rfind('Emma')
print(index)
#16
s = 'Emma-is-a-data-scientist'
result = ' '.join(s.split('-'))
print(result)
#17
s = '/*Jon is @developer & musician!!'
result = ''.join(char for char in s if char.isalpha() or char == ' ')
print(result)
#18
s = 'Apple'
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)
#19
str = 'Python is fun'
strArr=str.split(" ")
newStr=""
for i in strArr:
    rev=i[::-1]
    newStr=newStr+" "+rev
print(newStr.lstrip())
#20
s = '(())()'

count = 0
balanced = True

for char in s:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
    
    if count < 0:
        balanced = False
        break

if count == 0 and balanced:
    print("Balanced")
else:
    print("Not Balanced")