import re
from constants import VOID_TAGS

class Token:
    def __init__(self, name, token_type, line):
        self.name = name
        self.type = token_type
        self.line = line

class HTMLTokenizer:
    def __init__(self, html_content):
        self.html = html_content

    def tokenize(self):
        tokens = []
        pattern = re.compile(r"<[^>]+>")
        #enumerate(...., start=1) counts line number starting from 1
        for line_number, line_text in enumerate(self.html.splitlines(), start = 1):
            for match in pattern.finditer(line_text):
                raw_tag = match.group(0)
                line = line_number

                inner_content = raw_tag.strip("<>").strip()
                if inner_content.startswith("!"): #Skip comments or !DOCTYPE declaration
                    continue

                if raw_tag.startswith("</"):
                    token_type = "CLOSE"
                    tag_name = inner_content[1:].strip().split()[0].lower()

                elif raw_tag.endswith("/>"):
                    token_type = "VOID"
                    tag_name = inner_content[:-1].strip().split()[0].lower()
                else:
                    tag_name = inner_content.split()[0].lower()
                    if tag_name in VOID_TAGS:
                        token_type = "VOID"
                    else:
                        token_type = "OPEN"

                tokens.append(Token(tag_name, token_type, line))

        return tokens

