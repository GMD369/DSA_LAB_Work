class ExpressionEvaluator:

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    @staticmethod
    def is_operator(c):
        return c in '+-*/^'

    @staticmethod
    def infix_to_postfix(expression):


        
        stack = []
        postfix = []
        for char in expression:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] != '(' and ExpressionEvaluator.precedence[char] <= \
                        ExpressionEvaluator.precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:
            postfix.append(stack.pop())

        return ''.join(postfix)

    @staticmethod
    def evaluate_postfix(expression):
        stack = []
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                elif char == '/':
                    stack.append(a / b)
        return stack[0]

# Example
infix_expr = "(5+3)*(2-1)"
postfix_expr = ExpressionEvaluator.infix_to_postfix(infix_expr)
result = ExpressionEvaluator.evaluate_postfix(postfix_expr)

print("Postfix:", postfix_expr, "| Result:", result)


def infix_to_prefix(expression):
    # Reverse the expression and swap parentheses
    reversed_expr = expression[::-1]
    reversed_expr = reversed_expr.replace('(', ')temp').replace(')', '(').replace(')temp', ')')
    postfix = ExpressionEvaluator.infix_to_postfix(reversed_expr)
    return postfix[::-1]

# Example
infix_expr = "(a+b)*c"
prefix_expr = infix_to_prefix(infix_expr)
print("Prefix:", prefix_expr)


def logical_to_postfix(expression):
    return ExpressionEvaluator.infix_to_postfix(expression)

# Example
query = "(a AND b) OR c"
postfix_query = logical_to_postfix(query.replace("AND", "&").replace("OR", "|"))
print("Postfix Logical Query:", postfix_query)




variables = {'X': 10, 'Y': 5, 'Z': 2}

def evaluate_postfix_with_vars(expression, variables):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(variables.get(char, int(char)))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            
            elif char == '*':
                stack.append(a * b)
            
    return stack[0]  

# Example
postfix_expression = "XY+Z*"
result = evaluate_postfix_with_vars(postfix_expression, variables)
print("Result:", result)


def chatbot_response(query):
    expression = query.replace("What is", "").strip("?")
    postfix = ExpressionEvaluator.infix_to_postfix(expression)
    result = ExpressionEvaluator.evaluate_postfix(postfix)
    return f"The result is {result}"

# Example
query = "What is (10+5)*2?"
response = chatbot_response(query)
print(response)



class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def prefix_to_tree(expression):
    stack = []
    for char in reversed(expression):
        if char.isalnum():
            stack.append(Node(char))
        else:
            node = Node(char)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[0]

def inorder_traversal(node):
    if not node:
        return ""
    return inorder_traversal(node.left) + node.value + inorder_traversal(node.right)

# Example
prefix_expr = "-+a*bc"
root = prefix_to_tree(prefix_expr)
print("Infix from Prefix Tree:", inorder_traversal(root))

def evaluate_rpn(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack[0]  


# Example
rpn_expression = "100 20 + 5 /"
result = evaluate_rpn(rpn_expression)
print("Result:", result)