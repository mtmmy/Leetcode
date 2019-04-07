from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips)
        result = [clips[0]]
        if result[0][0] > 0:
            return -1
        for c in clips[1:]:
            if result[-1][1] >= T:
                break
            if c[0] > result[-1][1]:
                return -1
            if result[-1][0] == c[0] and result[-1][1] < c[1]:
                result[-1] = c
            elif c[1] <= result[-1][1]:
                continue
            elif c[0] <= result[-1][0]:
                result[-1] = [result[-1][0], c[1]]
            else:
                result.append([result[-1][1], c[1]])
        return len(result) if result[-1][1] >= T else -1
            