class HTMLValidator:
    def validate(self, tokens):
        stack = []

        for token in tokens:
            if token.type == "VOID":
                continue
            elif token.type == "OPEN":
                stack.append(token)
            elif token.type == "CLOSE":
                if not stack:
                    return (
                        False,
                        f"Syntax Error in [Line {token.line}]. Unexpected closing tag </{token.name}> with no opening tag."
                    )
                top = stack.pop()
                if top.name != token.name:
                    return (
                        False,
                        f"Syntax Error in [Line {token.line}]. Expected </{top.name}>, but found </{token.name}>"
                    )
            if stack:
                unclosed = stack[-1]
                return (
                    False,
                    f"Syntax Error. Unclosed tag <{unclosed.name}> in [Line {token.line}]. "
                )

            return True, "HTML Tag structure is valid"