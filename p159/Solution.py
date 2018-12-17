class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_dict = {}

        left_pointer = 0
        longest_length = 0

        for right_pointer in range(len(s)):
            current_char = s[right_pointer]
            if current_char not in char_dict:
                char_dict[current_char] = 0

            char_dict[current_char] += 1

            while len(char_dict) > 2:
                left_char = s[left_pointer]
                char_dict[left_char] -= 1
                if char_dict[left_char] == 0:
                    del char_dict[left_char]
                left_pointer += 1

            if right_pointer - left_pointer + 1 > longest_length:
                longest_length = right_pointer - left_pointer + 1

        return longest_length
