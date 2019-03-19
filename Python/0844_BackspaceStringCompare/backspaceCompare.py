class Solution:
    def backspaceCompare2Pointers(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        
        while True:
            while i >= 0 and (backS or S[i] == "#"):
                backS += 1 if S[i] == "#" else -1
                i -= 1
            while j >= 0 and (backT or T[j] == "#"):
                backT += 1 if T[j] == "#" else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i -= 1
            j -= 1
    
    def backspaceCompareStack(self, S: str, T: str) -> bool:
        stackS, stackT = [], []
        
        for c in S:
            if c == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
        
        for c in T:
            if c == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)
                
        return stackS == stackT