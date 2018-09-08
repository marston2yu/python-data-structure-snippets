# determine whether parenthesis in a string matches.

from pythonds.basic import Stack


def parChecker(str):
    s = Stack()
    for char in str:
        if char == '(':  # when encounter a left-parenthesis, push it to a stack.
            s.push(char)
        elif char == ')':  # when encounter a right-parenthesis,
            #  if the stack is empty, it means no matching left parenthesis.
            if s.isEmpty():
                return False
            else:
                s.pop()  # a right parenthesis can offset a left parenthesis in the stack.
    return s.isEmpty()  # finally, if the stack is clear, all parentheses match.
