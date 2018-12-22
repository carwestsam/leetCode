class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(people) == 0:
            return []
        elif len(people) == 1:
            return people

        order_people = []

        for [height, k] in people:
            order_people.append([-height, k])

        order_people.sort()

        result = []

        for [height, k] in order_people:
            result.insert(k, [-height, k])

        return result
