class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashtable
        # freq counter then sort
        # return splice by k
        # sorted(student_tuples, key=lambda student: student[2])
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        return [x for (x,y) in freq][:k]