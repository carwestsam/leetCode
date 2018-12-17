class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        formated_mails = []

        for email in emails:
            local, domain = email.split("@")

            local = (local + "+").split("+")[0]
            local = local.replace(".", "")

            formated_mails.append(local + "@" + domain)

        formated_mails.sort()

        formated_mails.append("")
        unique_mails = 0

        for i in range(len(formated_mails) - 1):
            if formated_mails[i] != formated_mails[i + 1]:
                unique_mails += 1

        return unique_mails
