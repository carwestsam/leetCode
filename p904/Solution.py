class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        left = 0
        cnt_dict = {}
        lt = len(tree)
        ans = 0

        for right in range(lt):
            v = tree[right]
            if v not in cnt_dict:
                cnt_dict[v] = 0
            cnt_dict[v] = cnt_dict[v] + 1

            while len(cnt_dict) > 2:
                tl = tree[left]
                cnt_dict[tl] = cnt_dict[tl] - 1
                if cnt_dict[tl] == 0:
                    del cnt_dict[tl]
                left += 1

            current_length = right - left + 1
            if current_length > ans:
                ans = current_length

        return ans
