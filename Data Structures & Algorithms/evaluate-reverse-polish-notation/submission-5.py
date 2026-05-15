class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opr = ["*","+","-","/"]
        operations = {

            "*": lambda x, y: x * y,
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: int(x / y)
        }

        for i in tokens:
            if i in opr:
                result = operations[i](int(stack[-2]),int(stack[-1]))
                # removing operands
                stack.pop()
                stack.pop()
                # adding result
                stack.append(result)
            else:
                stack.append(i)

        return int(stack[-1])