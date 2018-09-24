class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colored = [0] * n
        
        def drawColor(targets, color):
            for tar in targets:
                if colored[tar] == color:
                    return False
                elif colored[tar] == -color:
                    continue
                else:
                    colored[tar] = -color
                    if not drawColor(graph[tar], -color):
                        return False
            return True

        for i in range(n):
            edge = graph[i]
            color = colored[i] if colored[i] else 1
            if not drawColor(edge, color):
                return False
        
        return True