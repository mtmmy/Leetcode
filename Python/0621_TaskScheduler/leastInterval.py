from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
#         if n == 0:
#             return len(tasks)
        
#         intervals = 0
#         d = dict.fromkeys(string.ascii_uppercase, 0)
#         for t in tasks:
#             d[t] += 1
#         queue = []
#         result = []
#         sortedTasks = sorted(d, key = d.get, reverse = True)
        
        
#         counter = n + 1
#         while len(queue) == 0:
#             nonZeroCount = 0
#             for t in sortedTasks:
#                 if counter >=1 and d[t] > 0 and t not in queue:
#                     d[t] -= 1
#                     counter -= 1
#                     intervals += 1
#                     queue.append(t)
#                     result.append(t)
#                 else:
#                     break
#             sortedTasks = sorted(d, key = d.get, reverse = True)
#             if sum(d.values()) != 0:
#                 idles = ["idel"] * counter
#                 result.extend(idles)
#                 intervals += counter
#                 counter = n + 1
#                 queue.clear()
                
#         return intervals

        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        n_max = sum(freq == max_freq for freq in freqs.values())
        return max(len(tasks), (max_freq-1)*(n+1) + n_max)
            
            
        
            
        