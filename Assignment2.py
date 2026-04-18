# 1. Given: lst = [12, 45, 23, 67, 34] → Find max and min.
lst = [12, 45, 23, 67, 34]
print("maximum is :",max(lst))
print("maximum is :",min(lst))
# 2. Given: lst = [10, 20, 30] → Insert 25 at index 1
lst = [10, 20, 30]
lst.insert(1,25)
print(lst)
# 3. Given: lst = [5, 10, 15, 20] → Remove 15. 
lst = [5, 10, 15, 20]
lst.remove(15)
print(lst)
# 4. Given: lst = [9, 3, 7, 1] → Sort ascending. 
lst = [9, 3, 7, 1]
lst.sort()
print(lst)
# 5. Given: lst = [1, 2, 3, 4] → Reverse list. 
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)
# 6. Given: lst = [2, 4, 2, 6, 2] → Count 2. 
lst = [2, 4, 2, 6, 2]
print(lst.count(2))
# 7. Given: lst = [100, 200, 300] → Find index of 200.
lst = [100, 200, 300]
print(lst.index(200))
# 8. Given: lst1=[1,2], lst2=[3,4] → Merge lists.
lst1=[1,2]
lst2=[3,4]
lst3=lst1+lst2
print(lst3)
# 9. Given: lst=[11,22,33] → Check if 22 exists. 
lst=[11,22,33]
print(22 in lst)
# 10. Given: lst=[1,2,2,3,3] → Remove duplicates. 
lst=[1,2,2,3,3]
lst1=set(lst)
print(list(lst1))
# 11. Given: lst=[5,1,9,2] → Find second largest. 
lst=[5,1,9,2]
max1=max(lst)
lst.remove(max1)
print(max(lst))
#12. Given: lst=[10,20,30] → Replace 20 with 25
lst=[10,20,30]
pos=lst.index(20)
lst[pos]=25
print(lst)
# 13. Given: lst=[1,2,3] → Extend with [4,5]. 
lst=[1,2,3]
print(lst.extend([4,5]))
# 14. Given: lst=[7,8,9] → Pop last element.
lst=[7,8,9]
lst.pop()
print(lst)
# 15. Given: lst=[2,4,6,8] → Check if all even.
lst=[2,4,6,8]
all_even=True
for i in lst:
    if i%2==0:
        continue
    else:
        all_even=False
        break
print(all_even)


