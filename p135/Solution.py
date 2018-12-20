class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        rating_idx = [(rating, idx + 1) for idx, rating in enumerate(ratings)]
        ratings = [ratings[0]] + ratings + [ratings[-1]]
        rating_idx.sort()

        assignment = [1] * (2 + len(ratings))

        for rating, idx in rating_idx:
            if rating > ratings[idx - 1] and assignment[idx] < assignment[idx - 1] + 1:
                assignment[idx] = assignment[idx - 1] + 1
            if rating > ratings[idx + 1] and assignment[idx] < assignment[idx + 1] + 1:
                assignment[idx] = assignment[idx + 1] + 1

        return sum(assignment[1:len(rating_idx)+1])
