class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        len_seats = len(seats)
        seats.append(2)
        result = 1

        i = len_seats - 1
        while seats[i] == 0:
            i -= 1

        if len_seats - i - 1 > result:
            result = len_seats - i - 1

        i = 0
        while seats[i] == 0:
            i += 1

        if i > result:
            result = i

        while i < len_seats:
            while seats[i] == 1:
                i += 1
            j = i + 1
            while j < len_seats and seats[j] == 0:
                j += 1

            if j < len_seats and (j - i + 1) // 2 > result:
                result = (j - i + 1) // 2

            i = j

        return result
