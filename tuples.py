#tuples- same as list but immutable
#we cannot add/delete/edit items of an existing
week=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(week[1])
print(week[-1])

#we can reassign the entireeee tuple
week=('saturday')
print(week)

#len() to get number of items in a tuple
week=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(len(week))

#in operator to find if an item is in tuple
print("november" in week)

#del operator to delete an entire tuple
del week

week=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
#we can + or * tuple but it will not modify the original tuple
week1=('rowday')
print(week1+week)
