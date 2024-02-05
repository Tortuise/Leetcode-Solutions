class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers at start, end
        # add sum check if sum > or < than target
        # + 1 start if >, -1 end if <
        i,j = 0, len(numbers)-1
        res = []
        while (i < j):
            sum = numbers[i] + numbers[j]
            if (sum < target):
                i += 1
            elif (sum == target):
                res.append(i+1)
                res.append(j+1)
                break
            else:
                j -= 1
        return res
        