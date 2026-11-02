class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric()):
                stack.append(int(token))
            else:
                match token:
                    case '+':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1+num2)
                    case '-':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1-num2)
                    case '*':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1*num2)
                    case '/':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(int(num1/num2))
        
        return stack.pop()
                    