import unittest
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        times = time.split(":")
        hour = int(times[0])
        minite = int(times[1])
        nums = []
        for c in time:
            if c.isdigit():
                nums.append(int(c))
                
        hours = []
        minutes = []
        
        nums.sort()

        for i in nums:
            for j in nums:
                if i < 2:
                    hours.append(i * 10 + j)
                elif i == 2 and j < 5:
                    hours.append(i * 10 + j)

                if i < 6:
                    minutes.append(i * 10 + j)
                
        for i in hours:
            if i == hour:
                for j in minutes:
                    if j > minite:
                        return str(i).zfill(2) + ":" + str(j).zfill(2)
            elif i > hour:
                return str(i).zfill(2) + ":" + str(minutes[0]).zfill(2)
        
        return str(hours[0]).zfill(2) + ":" + str(minutes[0]).zfill(2)

        
        
class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        self.assertEqual("21:51", target.nextClosestTime("21:45"))
        self.assertEqual("21:02", target.nextClosestTime("21:01"))
        self.assertEqual("01:33", target.nextClosestTime("01:32"))
        self.assertEqual("19:39", target.nextClosestTime("19:34"))
        self.assertEqual("22:22", target.nextClosestTime("23:59"))

if __name__ == '__main__':
    unittest.main()