from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """        
        dictDegree = {key: 0 for key in [i for i in range(numCourses)]}
        dictPre = {key: [] for key in [i for i in range(numCourses)]}

        for pre in prerequisites:
            dictPre[pre[1]].append(pre[0])
            dictDegree[pre[0]] += 1
        
        queue = deque()
            
        for i in range(numCourses):
            if dictDegree[i] == 0:
                queue.append(i)
        
        while queue:
            t = queue.popleft()
            for num in dictPre[t]:
                dictDegree[num] -= 1
                if dictDegree[num] == 0:
                    queue.append(num)
                        
        for i in range(numCourses):
            if dictDegree[i] != 0:
                return False
        return True

                