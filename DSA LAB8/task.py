class ExpressionTransformer:
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def __init__(self, expr):
        self.expr = expr

    @staticmethod
    def is_operator(symbol):
        return symbol in ['+', '-', '*', '/', '^']

    @staticmethod
    def is_operand(symbol):
        return symbol.isalnum()

    def infix_to_postfix(self):
        operator_stack = []
        postfix_expr = []

        for token in self.expr:
            if self.is_operand(token):  # Add operand directly to postfix
                postfix_expr.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                # Pop operators until '(' is encountered
                while operator_stack and operator_stack[-1] != '(':
                    postfix_expr.append(operator_stack.pop())
                operator_stack.pop()  # Discard the '('
            else:
                # Pop operators with greater or equal precedence
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence_map[token] <= self.precedence_map.get(operator_stack[-1], 0)):
                    postfix_expr.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            postfix_expr.append(operator_stack.pop())  # Append remaining operators

        return ''.join(postfix_expr)

    def infix_to_prefix(self):
        reversed_expr = self.expr[::-1]
        adjusted_expr = (reversed_expr.replace('(', 'temp')
                                         .replace(')', '(')
                                         .replace('temp', ')'))

        postfix_form = ExpressionTransformer(adjusted_expr).infix_to_postfix()
        return postfix_form[::-1]

    def postfix_to_infix(self, postfix_expr):
        operand_stack = []

        for token in postfix_expr:
            if self.is_operand(token):
                operand_stack.append(token)
            else:
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
                operand_stack.append(f'({left_operand}{token}{right_operand})')

        return operand_stack[-1]

    def prefix_to_infix(self, prefix_expr):
        operand_stack = []

        for token in reversed(prefix_expr):
            if self.is_operand(token):
                operand_stack.append(token)
            else:
                left_operand = operand_stack.pop()
                right_operand = operand_stack.pop()
                operand_stack.append(f'({left_operand}{token}{right_operand})')

        return operand_stack[-1]


# Example usage
input_expression = "a+b*(c^d-e)^(f+g*h)-i"
transformer = ExpressionTransformer(input_expression)

print("Infix Expression:", input_expression)
postfix_result = transformer.infix_to_postfix()
print("Postfix Expression:", postfix_result)
prefix_result = transformer.infix_to_prefix()
print("Prefix Expression:", prefix_result)
print("Converted back to Infix from Postfix:", transformer.postfix_to_infix(postfix_result))
print("Converted back to Infix from Prefix:", transformer.prefix_to_infix(prefix_result))
