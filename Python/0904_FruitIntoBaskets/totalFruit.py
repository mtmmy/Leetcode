class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if len(tree) <= 2:
            return len(tree)
        # fstHead: head of the first kind of character
        # fstTail: tail of the first kind of character
        fstHead, fstTail, maxLen = 0, -1, 0

        # tracker: to track the change of characters
        for tracker in range(1, len(tree)):
            if tree[tracker] != tree[tracker - 1]:                
                if fstTail != -1 and tree[tracker] != tree[fstTail]:
                    maxLen = max(maxLen, tracker - fstHead)
                    fstHead = fstTail + 1
                fstTail = tracker - 1
        return max(maxLen, len(tree) - fstHead)
