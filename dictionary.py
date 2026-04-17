#Dictionary -  collection data types with key values
mystudents={'Tom':5,'Jerry':3,'mickey':4}
#the keys should be unique , values can have duplicates
#no access with index numbers

#access element using keys instead of index
print(mystudents['Jerry'])
#dictionary is mutable, we can add or delete items
mystudents['jerry']=7
print(mystudents)
#get() will get the value of the given key
print(mystudents.get('jerry'))
#get the list of all keys in the dictionary
print(mystudents.keys())
#get the list of all values in the dictionary
print(mystudents.values())
#get the list of all items
print(mystudents.items())
#to check if an key is there in the dictionary
print('Tom' in mystudents)
#to check if an value is there in the dictionary
print(30 in mystudents.values())
#update a dictionary with another dictionary
mystudents2={'superman':20,'ironman':35}
mystudents.update(mystudents2)
print(mystudents)
#delete a specific key value pair
mystudents.pop('mickey')
#will remove superman key and its value
mystudents.clear()
#clears the dictionary
print(mystudents)#{}


#use del operator to delete the entire dictionary
del mystudents

