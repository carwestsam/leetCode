class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        len_input = len(input)

        def readline(idx):
            pt = idx

            indents = 0
            content = ''

            if input[pt] == ' ':
                while input[pt] == ' ' and indents < 4:
                    pt += 1
                    indents += 1
                indents /= 4
            else:
                while input[pt] == '\t':
                    indents += 1
                    pt += 1

            while pt < len_input and input[pt] != '\n':
                content += input[pt]
                pt += 1

            while pt < len_input and input[pt] != '\n':
                pt += 1

            if pt < len_input and input[pt] == '\n':
                return (indents, content, '.' in content), pt + 1
            else:
                return (indents, content, '.' in content), pt

        ft = 0
        stack = []
        answer = ''
        while ft < len_input:
            (indent, content, is_file), ft = readline(ft)
            # print(indent, content, is_file)

            while len(stack) > indent:
                stack.pop()

            if is_file is True:
                filename = "/".join(stack + [content])
                # print(filename)
                if len(filename) > len(answer):
                    answer = filename
            else:
                stack.append(content)

        return len(answer)
