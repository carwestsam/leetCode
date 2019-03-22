from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if len(A) == 0:
            return -1
        ln = len(A)
        A.append(0)
        left = 0
        right = 0
        s = A[0]
        ans = ln + 1
        while right < ln:
            while left + 1 < right and s - A[left] >= K:
                s -= A[left]
                left = left + 1

            if right - left + 1 < ans and s >= K:
                ans = right - left + 1

            right = right + 1
            s += A[right]

        if ans == ln + 1:
            return -1

        return ans
