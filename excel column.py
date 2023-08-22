class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        base = 26
        res = columnNumber
        output = ""
        while (res > 0):
            res -= 1
            rem = res % base
            res = res // base
            
            
            output += a[rem]
            print('res',res,'rem',rem, output)
        return output[::-1]
