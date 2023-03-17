import re

# Define regular expressions for each token type
TOKENS = [
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('NUMBER', r'\d+'),
    ('STRING', r'"(\\.|[^"])*"'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('ASSIGN', r'='),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('COMMA', r','),
    ('NEWLINE', r'\n'),
    ('WHITESPACE', r'\s+'),
    ('COMMENT', r'//.*'),
    ('ERROR', r'.'),
]

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        while self.source_code:
            match = None
            for token in TOKENS:
                name, pattern = token
                regex = re.compile(pattern)
                match = regex.match(self.source_code)
                if match:
                    value = match.group(0)
                    self.tokens.append((name, value))
                    self.source_code = self.source_code[len(value):]
                    break
            if not match:
                print('Invalid character: %s' % self.source_code[0])
                self.tokens.append(('ERROR', self.source_code[0]))
                self.source_code = self.source_code[1:]
        return self.tokens
