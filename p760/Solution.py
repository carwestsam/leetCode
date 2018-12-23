class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        dic = {}

        for i in range(len(B)):
            if B[i] not in dic:
                dic[B[i]] = []
            dic[B[i]].append(i)

        ans = []
        for i in range(len(A)):
            ans.append(dic[A[i]].pop())

        return ans
