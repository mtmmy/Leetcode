import unittest

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        def collision(asteroid1, asteroid2):
            if asteroid1 + asteroid2 == 0:
                return 0
            return asteroid1 if abs(asteroid1) > abs(asteroid2) else asteroid2                

        result = []        
        for num in asteroids:
            if len(result) == 0:
                result.append(num)
            else:
                lastAsteroid = result[-1]
                if lastAsteroid < 0:
                    result.append(num)
                elif lastAsteroid > 0 and num > 0:
                    result.append(num)
                else:
                    while 1:                     
                        winner = collision(lastAsteroid, num)
                        if winner == 0:
                            result.pop()
                            break
                        elif winner == lastAsteroid:
                            break
                        else:
                            result.pop()
                            if len(result) == 0 or result[-1] < 0:
                                result.append(num)
                                break
                            lastAsteroid = result[-1]
        return result

class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual([5, 10], target.asteroidCollision([5, 10, -5]))
        self.assertEqual([], target.asteroidCollision([8, -8]))
        self.assertEqual([-1,-1,-2], target.asteroidCollision([-1,-1,1,-2]))
        self.assertEqual([-2,-2,-2], target.asteroidCollision([1,-2,-2,-2]))
        
if __name__ == '__main__':
    unittest.main()
    