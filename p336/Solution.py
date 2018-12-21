class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        word_list = []
        ans_dict = {}
        answers = []

        def palindrome(a):
            return a == a[::-1]

        for i in range(len(words)):
            word = words[i]
            ans_dict[i] = set()

            if word == "":
                for j in range(len(words)):
                    if i != j and palindrome(words[j]):
                        answers.append([j, i])
                        answers.append([i, j])

            else:
                word_list.append([word, 0, i])
                word_list.append([word[::-1], 1, i])

        word_list.sort()

        len_wl = len(word_list)
        for i in range(len_wl):
            [wa, ta, ia] = word_list[i]
            la = len(wa)

            j = i + 1
            while j < len_wl:
                [wb, tb, ib] = word_list[j]
                if len(wb) < la or wb[:la] != wa:
                    break

                if tb != ta and ia != ib:
                    if ib not in ans_dict[ia] and palindrome(words[ia] + words[ib]):
                        answers.append([ia, ib])
                        ans_dict[ia].add(ib)

                    if ia not in ans_dict[ib] and palindrome(words[ib] + words[ia]):
                        answers.append([ib, ia])
                        ans_dict[ib].add(ia)

                j = j + 1

        return answers
