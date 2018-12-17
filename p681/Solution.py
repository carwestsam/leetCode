class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        [hour, minute] = time.split(":")

        hour = int(hour)
        minute = int(minute)

        digits = {}

        for num in self.getNumbers(hour):
            digits[num] = True

        for num in self.getNumbers(minute):
            digits[num] = True

        while True:
            hour, minute = self.tick(hour, minute)
            if self.isValid(hour, minute, digits):
                break

        next_valid_moment = self.convert(hour) + ":" + self.convert(minute)
        return next_valid_moment

    def getNumbers(self, num_str):
        num = int(num_str)
        return [num // 10, num % 10]

    def tick(self, hour, minute):
        if minute < 59:
            return hour, minute + 1
        elif minute == 59:
            if hour < 23:
                return hour + 1, 0
            else:
                return 0, 0

    def isValid(self, hour, minute, digits):
        for num in [hour // 10, hour % 10, minute // 10, minute % 10]:
            if num not in digits:
                return False

        return True

    def convert(self, time):
        return str(time // 10) + str(time % 10)
