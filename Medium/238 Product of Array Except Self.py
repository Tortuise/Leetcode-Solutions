class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # double prefix left and right
        # rolling product from left and from right
        # would be o(n) time and O(1) space complex since output array doesnt count

        l = 0
        r = len(nums) - 1
        lprod = 1
        rprod = 1
        arr = [1 for i in range(len(nums))]

        while (l < len(nums)-1):
            lprod = nums[l] * lprod
            arr[l+1] *= lprod

            l += 1

        while (r > 0):
            rprod = nums[r] * rprod
            arr[r-1] *= rprod
            r -= 1

        print(arr)
        return arr
