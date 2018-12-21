class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        len_intervals = len(intervals)

        if len_intervals <= 1:
            return len_intervals

        def start_time(elem):
            return elem.start

        intervals.sort(key=start_time)

        end_list = [intervals[0].end]

        i = 1
        while i < len_intervals:
            current_start = intervals[i].start

            j = 0

            while j < len(end_list):
                if current_start >= end_list[j]:
                    end_list[j] = intervals[i].end
                    break

                j += 1

            if j == len(end_list):
                end_list.append(intervals[i].end)

            i += 1

        return len(end_list)
