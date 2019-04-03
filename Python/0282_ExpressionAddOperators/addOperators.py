from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:        
        result = []
        def dfs(formula, pos, ans, multi):
            """
                Parameters:
                formula: formed formula so far
                pos: position of the string num
                ans: the answer of the formula
                multi: the number we may need to multiply
            """
            if pos == len(num):
                if ans == target:
                    result.append(formula)
                return
            
            for i in range(pos, len(num)):
                # ignore numbers starting from 0
                if i != pos and num[pos] == "0":
                    break
                curStr = num[pos:i + 1]
                cur = int(curStr)
                if pos == 0:
                    dfs(formula + curStr, i + 1, cur, cur)
                else:
                    dfs(formula + "+" + curStr, i + 1, ans + cur, cur)
                    dfs(formula + "-" + curStr, i + 1, ans - cur, -cur)
                    
                    # take out the last number and multiply it by the current number
                    dfs(formula + "*" + curStr, i + 1, ans - multi + multi * cur, multi * cur)
                    
        dfs("", 0, 0, 0)
        return result