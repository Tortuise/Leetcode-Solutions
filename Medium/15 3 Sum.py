class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]

        
        nums.sort()
        trips = []

        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    trips.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
        print(trips)
        return trips