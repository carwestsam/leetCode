class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        cleaned_S = S.replace("-", "").upper()
        len_s = len(cleaned_S)

        if len_s == 0 or K >= len_s:
            return cleaned_S

        left_pointer = len_s % K
        if left_pointer == 0:
            left_pointer += K

        license = cleaned_S[: left_pointer]

        while left_pointer < len_s:
            license += "-" + cleaned_S[left_pointer: left_pointer + K]
            left_pointer += K

        return license
