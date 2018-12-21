class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def get_start(elem):
            return elem.start

        intervals.sort(key=get_start)

        results = []

        i = 0
        len_intervals = len(intervals)
        while i < len_intervals:
            j = i + 1
            while j < len_intervals and intervals[j].start <= intervals[i].end:
                if intervals[j].end > intervals[i].end:
                    intervals[i].end = intervals[j].end
                j += 1
            results.append(intervals[i])
            i = j

        return results
