class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # break all words into letters
        # sort all letters in words into alphabetical order
        # group all words together if they have same letter using dictionary key is sorted letters, value is words
        dict = {}
        for i in range(len(strs)):
            letters = (strs[i].strip(""))
            letters = "".join(sorted(letters))
            if letters in dict:
                dict[letters].append(strs[i])
            else:
                dict[letters] = [strs[i]]
 
        return dict.values()
