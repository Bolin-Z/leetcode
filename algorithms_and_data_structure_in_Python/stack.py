import string

class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("ERROR: CAN NOT POP AN EMPTY STACK")
    
    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            print("ERROR: CAN NOT PEAK AN EMPTY STACK")
    
    def size(self):
        return len(self.items)

class ParChecker:
    @staticmethod
    def parChecker(symbolString:str) -> bool:
        s = Stack()
        balanced = True
        index = 0
        while index < len(symbolString) and balanced:
            symbol = symbolString[index]
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    top = s.pop()
                    if not ParChecker.__matches(top, symbol):
                        balanced = False
            index += 1
        return balanced and s.isEmpty()
    
    @staticmethod
    def __matches(open, close) -> bool:
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

class BaseConverter:
    @staticmethod
    def baseConverter(decNumber:int, b:int = 2) -> str:
        """
        Convert demical number into base-b number string
        :param decNumber: demical number to be converted
        :param b: target base, range from 2 to 16
        :return: return target base-b number string
        """
        digits = "0123456789ABCDEF"
        remstack = Stack()

        while decNumber > 0:
            rem = decNumber % b
            remstack.push(rem)
            decNumber = decNumber // b
        
        newString = ""
        while not remstack.isEmpty():
            newString += digits[remstack.pop()]
        
        return newString

class Expression:
    @staticmethod
    def infixToPostfix(infixexpr:str) -> str:
        prec = {
            "*" : 3, "/" : 3,
            "+" : 2, "-" : 2,
            "(" : 1
        }

        opStack = Stack()
        postfixList = []

        tokenList = infixexpr.split()

        for token in tokenList:
            if token in string.ascii_uppercase:
                postfixList.append(token)
            elif token == "(":
                opStack.push(token)
            elif token == ")":
                topToken = opStack.pop()
                while topToken != "(":
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
            
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        
        return " ".join(postfixList)

    @staticmethod
    def postfixEval(postfixExpr:str):
        operandStack = Stack()

        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = Expression.__doMath(token, operand1, operand2)
                operandStack.push(result)

        return operandStack.pop()

    @staticmethod
    def __doMath(op, operand1, operand2):
        if op == "*":
            return operand1 * operand2
        elif op == "/":
            return operand1 / operand2
        elif op == "+":
            return operand1 + operand2
        else:
            return operand1 - operand2

if __name__ == "__main__":
    testList = [
        "( A + B ) * ( C + D )",
        "( A + B ) * C",
        "A + B * C"
    ]

    for x in testList:
        print(x)
        print("  ", Expression.infixToPostfix(x))