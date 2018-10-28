import heapq
class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key=lambda x: x[1])
        curTime, courseHeap = 0, []
        
        for d, e in courses:
            curTime += d
            heapq.heappush(courseHeap, -d)
            if curTime > e:
                curTime -= -heapq.heappop(courseHeap)
        
        return len(courseHeap)