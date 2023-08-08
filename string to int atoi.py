class Solution:
    def myAtoi(self, s: str) -> int:
        # dfa

        state = 0
        i = 0
        sign = 1
        value = []
        
        while i < len(s):
            if state == 0:
                if s[i].isdigit():
                    value.append(s[i])
                    state = 2
                elif s[i] == "+" or s[i] == "-":
                    if s[i] == "-":
                        sign *= -1
                    state = 1
                elif s[i] == " ":
                    state = 0
                else:
                    return 0
            elif state == 1:
                if s[i].isdigit():
                    value.append(s[i])
                    state = 2
                else:
                    return 0
            elif state == 2:
                if not s[i].isdigit():
                    break
                else:
                    value.append(s[i])
            i += 1
        print(s)
        print(value)
        print(sign)
        if not value:
            return 0
        value = int("".join(value))
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value