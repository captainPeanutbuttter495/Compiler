# import reg expression mod for regex matching
import re

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type!r}, {self.value!r})"
        return f"Token({self.type!r})"

TOKEN_PATTERNS = [
    (re.compile(r"\bint\b"), "KEYWORD"),
    (re.compile(r"\bvoid\b"), "KEYWORD"),
    (re.compile(r"\breturn\b"), "KEYWORD"),
    (re.compile(r"[a-zA-Z_]\w*\b"), "IDENT"),
    (re.compile(r"[0-9]+\b"), "CONSTANT"),
    (re.compile(r"\("), "LPAREN"),
    (re.compile(r"\)"), "RPAREN"),
    (re.compile(r"\{"), "LBRACE"),
    (re.compile(r"\}"), "RBRACE"),
    (re.compile(r";"), "SEMICOLON"),
]

# function to take entire string input
def tokenize(input_string):
    # init an empty list to collect Token objects
    tokens = []

    while len(input_string) > 0:
        # skip whitespace
        if input_string[0].isspace():
            input_string = input_string[1:]

        else:
            matched = False

            # scans for tokens
            for regex, token_type in TOKEN_PATTERNS:
                # checks current string starts with regex token pattern
                match = regex.match(input_string)
                # match found, group exact matched text
                if match:
                    matched = True
                    matched_text = match.group()

                    # check if token needs to store values 
                    # i.e var names or numbers
                    if token_type in ("IDENT", "CONSTANT"):
                        tokens.append(Token(token_type, matched_text))

                    else:
                        tokens.append(Token(token_type))

                    # remove matched part
                    input_string = input_string[len(matched_text):]
                    break

            if not matched:
                raise Exception("Unrecognized token: " + input_string)

    return tokens
