# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums)):
#                 if j==i:
#                     continue
#                 else:
#                    print("===",nums[i],nums[j])
#                    if(nums[i]+nums[j]==target):
#                         return [i,j]
                   
# print(twoSum([3,2,4],6))

# def isPalindrome(x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x<0:
#             return False
#         else:
#             if x[::-1] ==x:
#                 return True
#             else :
#                 return False
# print(isPalindrome(121))
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
romanToNumber={
    "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
}
def roman(s):
    if romanToNumber.get(s[0])>romanToNumber.get(s[len(s)-1]):
        print("leftToRight")
        return leftToRight(s)
    else:
        print("rightToLeft")
        return rightToLeft(s)

def leftToRight(s):
    add=0
    for i in s:
        add+=romanToNumber.get(i)
    return add

def rightToLeft(s):
    add=0
    for i in s[::-1]:
        if i==s[len(s)-1]:
            add+=romanToNumber.get(i)
        else:
            add-=romanToNumber.get(i)
    return add

print(roman("MCMXCIV"))



        