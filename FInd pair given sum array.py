#FInd pair given sum array
nums = [8, 7, 2, 5, 3, 1]
target = 10
# https://medium.com/techie-delight/top-50-classic-data-structures-problems-2a2f68ba924c
# using hashmap dictionary take a num1 and find target - num2 in dictionary to get num1 + num2 = target
# Hashmap most optimal O(n) time complexity and O(n) space complexity
def findPair(nums, target):
    d = {}
    for i,e in enumerate(nums):

        if target - e in d:
            return (e, nums[d.get(target - e)])
        d[e] = i
        print(d)
    print("pair not found")
    return

print(findPair(nums,target))


