class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        seq = 1
        currseq = 1
        for i in range(1,len(nums)):
            if ((nums[i-1] + 1) == nums[i]):
                currseq += 1

            else:
                seq = max(seq,currseq)
                currseq = 1
        seq = max(seq, currseq)
        print(nums)
        return seq
