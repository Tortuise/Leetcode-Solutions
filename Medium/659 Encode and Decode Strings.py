class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    """
    @param: str: A string
    @return: dcodes a single string to a list of stirngs.
    """
    def decode(self, str):
        res = []
        i = 0
        while (i < len(str)):
            j = i
            while (str[j] != "#"):
                j += 1
            length = int(str[i:j])
            s = str[j+1:j+length+1]
            res.append(s)
            i = j + 1 + length
        return res



