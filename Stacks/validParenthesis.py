class Solution:
    def isValid(self, s: str) -> bool:
        total = []

        if (len(s)%2) != 0:
            return False

        for i in s:
            if i == "[" or i == "{" or i == "(":
                total.append(i)
            elif not total:
                return False
            elif i == ']' and total[-1] != "[":
                return False
            elif i == '}' and total[-1] != "{":
                return False
            elif i == ')' and total[-1] != "(":
                return False
            else:
                total.pop()
            
        
        return len(total) == 0