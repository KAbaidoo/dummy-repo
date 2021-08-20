# Description: program converts infix to postfix notation
import sys

# creating a stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)


class InfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = Stack()
        output = ''

        for c in expr:
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()
                else:
                    while (not self.stack.isEmpty()) and self.hasLessOrEqualPriority(c, self.stack.peek()):
                        output += self.stack.pop()
                    self.stack.push(c)

        while not self.stack.isEmpty():
            output += self.stack.pop()
        return output

    def convert(self, expr):
        try:
            result = eval(expr);
        except:
            result = expr
        print('Original expr is: {}\nPostfix is: {}\nresult is: {}'.format(expr, self.toPostfix(expr), result))

def main(argv):
    infix = InfixConverter()
    infix_expression = input("Enter an expression in infix notation or 'exit' to stop: ")
    if infix_expression.lower() == 'exit':
        exit()
    else:
        infix.convert(infix_expression)

if __name__ == "__main__":
    main(sys.argv)
