class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.result = []

    def generate_code(self):
        for node in self.ast:
            if node[0] == 'ASSIGNMENT':
                self.generate_assignment(node)
            elif node[0] == 'PRINT':
                self.generate_print(node)
            else:
                raise Exception('Unknown node type: %s' % node[0])
        return '\n'.join(self.result)

    def generate_assignment(self, node):
        var_name, expr = node[1], node[2]
        expr_code = self.generate_expr(expr)
        self.result.append('%s = %s' % (var_name, expr_code))

    def generate_print(self, node):
        expr = node[1]
        expr_code = self.generate_expr(expr)
        self.result.append('print(%s)' % expr_code)

    def generate_expr(self, node):
        if isinstance(node, tuple):
            op, left, right = node
            left_code = self.generate_expr(left)
            right_code = self.generate_expr(right)
            return '(%s %s %s)' % (left_code, op, right_code)
        elif isinstance(node, str):
            return node
        else:
            raise Exception('Unknown node type: %s' % type(node).__name__)
