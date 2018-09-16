import unittest

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations or not queries:
            return []
            
        mapper = {}

        def dfs(current, path, target, allPath):
            if target in mapper[current]:
                newPath = path.copy()
                newPath.append(target)  
                allPath.append(newPath)
            else:
                for letter in mapper[current]:
                    if letter not in path:
                        newPath = path.copy()
                        newPath.append(letter)
                        dfs(letter, newPath, target, allPath)
            
        
        for eq, val in zip(equations, values):
            if eq[0] not in mapper:
                mapper[eq[0]] = {eq[1]: val}
            else:
                mapper[eq[0]][eq[1]] = val

            if eq[1] not in mapper:
                mapper[eq[1]] = {eq[0]: 1/val}
            else:
                mapper[eq[1]][eq[0]] = 1/val

        result = []
        for query in queries:
            if query[0] not in mapper or query[1] not in mapper:
                result.append(-1.0)
            elif query[0] == query[1]:
                result.append(1.0)
            else:
                if query[1] in mapper[query[0]]:
                    result.append(mapper[query[0]][query[1]])
                else:
                    allPath = []
                    dfs(query[1], [query[1]], query[0], allPath)
                    
                    if not allPath:
                        result.append(-1.0)
                    else:
                        path = allPath[0]
                        cur = path.pop()
                        next = path.pop()
                        prod = mapper[cur][next]
                        while path:                            
                            cur = next
                            next = path.pop()
                            prod *= mapper[cur][next]
                        result.append(prod)
        return result

        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = [6.0, 0.5, -1.0, 1.0, -1.0 ]
        test = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
        self.assertEqual(expected, target.calcEquation([["a", "b"], ["b", "c"],["c","e"]], [2.0,3.0,4.0], test))

if __name__ == '__main__':
    unittest.main()
        