from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrderBFS_one_dict(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(set)        
        queue = deque()
        
        for c1, c2 in prerequisites:
            courses[c1].add(c2)
            
        for i in range(numCourses):
            if i not in courses:
                queue.append(i)
        
        result = []
        while queue:
            nextLevel = []
            while queue:
                cur = queue.popleft()
                result.append(cur)
                for key, val in courses.items():                    
                    if cur in val:
                        val.remove(cur)
                        if not val:
                            nextLevel.append(key)
            for c in nextLevel:
                del courses[c]
            queue += nextLevel
        return result if len(result) == numCourses else []
    
    def findOrderBFS_two_dict(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        outdegree = defaultdict(set)
        indegree = defaultdict(list)
        queue = deque()
        
        for c1, c2 in prerequisites:
            outdegree[c1].add(c2)
            indegree[c2].append(c1)
            
        for i in range(numCourses):
            if i not in outdegree:
                queue.append(i)
        
        result = []
        while queue:
            nextLevel = []
            while queue:
                cur = queue.popleft()
                result.append(cur)               
                for n in indegree[cur]:
                    outdegree[n].remove(cur)
                    if not outdegree[n]:
                        del outdegree[n]
                        nextLevel.append(n)
            queue += nextLevel
        return result if len(result) == numCourses else []