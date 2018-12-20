class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        self.visited = set()
        self.directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        self.robot = robot
        self.dfs(0, 0, 0)

    def dfs(self, x, y, direction):
        self.visited.add((x, y))
        self.robot.clean()
        for i in range(4):
            next_x = x + self.directions[direction][0]
            next_y = y + self.directions[direction][1]
            if (next_x, next_y) not in self.visited and self.robot.move():
                self.dfs(next_x, next_y, direction)
                self.robot.turnRight()
                self.robot.turnRight()
                self.robot.move()
                self.robot.turnRight()
                self.robot.turnRight()

            self.robot.turnRight()
            direction = (direction + 1) % 4
