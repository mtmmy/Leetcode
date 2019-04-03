class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(i, j, d):
            robot.clean()
            visited.add((i, j))
            for k in range(4):
                newD = (d + k) % 4
                di, dj = directions[newD]
                di, dj = i + di, j + dj
                if  (di, dj) not in visited and robot.move():
                    dfs(di, dj, newD)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                    robot.turnLeft()
                robot.turnLeft()
        dfs(0, 0, 0)