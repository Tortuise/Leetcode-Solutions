class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # i = 0
        # for range len nums:
        # length array is target, index = len-1
        # loop through nums 
        # for i=0 run range 2
        # specify i < length
        # if youre increasing index in any way in j range possible positions
        # if it is a possible position you can go there
        # 0 at index 4 it cant go any further than fail it
        
        # end = len(nums) - 1
        # if (len(nums) == 1):
        #     return True
        # if (nums[0] == 0):
        #     return False
        # i = 0
        # while (i <= end):
        #     max_jump = nums[i]
        #     if (max_jump >= end):
        #         return True
            
        #     possible = False
        #     next_pos = 0
        #     for j in range(i+1,i+max_jump+1):
        #         potential_position = j + nums[j] 
        #         if (potential_position >= end):
        #             return True
        #         if (nums[j] < 1 and not possible):
        #             possible=False
        #         elif (nums[j] < 1):
        #             continue
        #         else: 
        #             possible=True
        #             next_pos = j
        #             print(next_pos)


        #     if (not possible):
        #         return False
        #     else:
        #         i = next_pos
        
        # return False

        end = len(nums) - 1
        j = end
        for i in range(j,-1, -1):
            # if find number that reaches end
            if (i + nums[i] >= j):
                j = i
            if (j == 0):
                return True
        return False