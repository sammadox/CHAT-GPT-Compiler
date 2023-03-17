from lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        ast = self.parse_program()
        if self.current_token()[0] != 'EOF':
            self.error('Unexpected token: %s' % self.current_token()[1])
        return ast

    def parse_program(self):
        program = []
        while self.current_token()[0] != 'EOF':
            statement = self.parse_statement()
            if statement:
                program.append(statement)
        return program

    def parse_statement(self):
        token_type = self.current_token()[0]
        if token_type == 'IDENTIFIER':
            return self.parse_assignment()
        elif token_type == 'PRINT':
            return self.parse_print()
        else:
            self.error('Unexpected token: %s' % self.current_token()[1])

    def parse_assignment(self):
        identifier = self.consume('IDENTIFIER')
        self.consume('ASSIGN')
        expr = self.parse_expression()
        self.consume('NEWLINE')
        return ('ASSIGNMENT', identifier[1], expr)

    def parse_print(self):
        self.consume('PRINT')
        expr = self.parse_expression()
        self.consume('NEWLINE')
        return ('PRINT', expr)

    def parse_expression(self):
        expr = self.parse_term()
        while self.current_token()[0] in ('PLUS', 'MINUS'):
            op = self.consume(self.current_token()[0])
            right = self.parse_term()
            expr = (op[1], expr, right)
        return expr

    def parse_term(self):
        term = self.parse_factor()
        while self.current_token()[0] in ('MULTIPLY', 'DIVIDE'):
            op = self.consume(self.current_token()[0])
            right = self.parse_factor()
            term = (op[1], term, right)
        return term

    def parse_factor(self):
        token_type, token_value = self.current_token()
        if token_type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
            return expr
        elif token_type == 'IDENTIFIER':
            return self.consume('IDENTIFIER')
        elif token_type == 'NUMBER':
            return self.consume('NUMBER')
        elif token_type == 'STRING':
            return self.consume('STRING')
        else:
            self.error('Unexpected token: %s' % token_value)

    def consume(self, expected_token_type):
        token = self.current_token()
        if token[0] == expected_token_type:
            self.pos += 1
            return token
        else:
            self.error('Expected token: %s, found: %s' % (expected_token_type, token[0]))

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')

    def error(self, message):
        raise Exception('Parse error: %s' % message)
