# transform a arithmetic expression between infix, postfix and prefix.

from pythonds.basic import Stack


# check order of two operators.
def isSuperiorOrEqual(op1, op2):
    if op1 in ['+', '-'] and op2 in ['*', '/']:
        return False
    return True


# transform infix expression to postfix expression.
def infixToPostfix(infixexpr):
    exprList = infixexpr.split(' ')
    output = []
    opStack = Stack()

    for token in exprList:
        if token == '(':
            opStack.push(token)
        elif token == ')':  # pop until find the left-parenthesis.
            while True:
                op = opStack.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif token in ['+', '-', '*', '/']:
            # pop superior or equal operators then push operator.
            # do not pop `(` here.
            while not opStack.isEmpty() and opStack.peek() != '(':
                if isSuperiorOrEqual(opStack.peek(), token):
                    output.append(opStack.pop())
                else:
                    break
            opStack.push(token)
        else:
            output.append(token)

    # retrieve the remain marks in operation stack.
    while not opStack.isEmpty():
        output.append(opStack.pop())
    return ' '.join(output)


# transform infix expression to prefix expression.
# reverse expression list and swap the mark `(` and `)`.
# in the end, reverse output.
def infixToPrefix(infixexpr):
    exprList = infixexpr.split(' ')
    exprList.reverse()
    output = []
    opStack = Stack()

    for token in exprList:
        if token == ')':
            opStack.push(token)
        elif token == '(':  # pop until find the left-parenthesis.
            while True:
                op = opStack.pop()
                if op == ')':
                    break
                else:
                    output.append(op)
        elif token in ['+', '-', '*', '/']:
            # pop superior or equal operators then push operator.
            # do not pop `)` here.
            while not opStack.isEmpty() and opStack.peek() != ')':
                if isSuperiorOrEqual(opStack.peek(), token):
                    output.append(opStack.pop())
                else:
                    break
            opStack.push(token)
        else:
            output.append(token)

    # retrieve the remain marks in operation stack.
    while not opStack.isEmpty():
        output.append(opStack.pop())

    output.reverse()  # output is a reverse of prefix as a result of beginning reverse operation.
    return ' '.join(output)


def evalPostfix(postfixExpr):
    exprList = postfixExpr.split(' ')
    operandStack = Stack()

    for token in exprList:
        if token == '+':
            operandStack.push(operandStack.pop() + operandStack.pop())
        elif token == '-':  # in minus, calculation order is opposite to pop order.
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            operandStack.push(operand2 - operand1)
        elif token == '*':
            operandStack.push(operandStack.pop() * operandStack.pop())
        elif token == '/':  # in division, calculation order is opposite to pop order.
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            operandStack.push(operand2 / operand1)
        else:
            operandStack.push(float(token))

    return operandStack.pop()


if __name__ == '__main__':
    print(infixToPostfix('A * B + C * D'))
    print(evalPostfix('7 8 + 3 2 - /'))
    print(infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))
    print(infixToPrefix('( A + B ) * C - ( D - E ) * ( F + G )'))
