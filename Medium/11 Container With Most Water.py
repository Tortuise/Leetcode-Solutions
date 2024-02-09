class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxVol = 0
        # fix j check area
        # if height i less than height j then i++
        # else j-- 
        while (i < j):
            # fix i
            
            l1 = height[i]
            l2 = height[j]

            lmin = min(l1,l2)
            width = abs(j-i)
            vol = width * lmin
            maxVol = max(maxVol,vol)
            print(i,j)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return maxVol
        