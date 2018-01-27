import operator 
 
def execute(expr):
    OPERATOR_TO_LAMBDA = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv} 
    stack = [0] 
    for token in expr.split(" "): 
        if token in OPERATOR_TO_LAMBDA: 
            op2, op1 = stack.pop(), stack.pop() 
            if token == '/':
 
                 if isinstance(op1,int):
                        stack.append(operator.floordiv(op1,int(op2)))
                 else:
                        stack.append(OPERATOR_TO_LAMBDA[token](op1,op2))
            else:
                 stack.append(OPERATOR_TO_LAMBDA[token](op1,op2))
        elif token.isdigit():
            stack.append(int(token))
        else:
            stack.append(float(token))
    return stack.pop()
