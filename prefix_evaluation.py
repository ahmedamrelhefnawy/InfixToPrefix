from stack import stack
from infix_to_prefix import infix_to_prefix
from domath import domath


def prefixEvaluation(infixExpr):  # Postfix should have spaces as separators
    opStack = stack()
    tokenList = infix_to_prefix(infixExpr).split()[::-1]

    for token in tokenList:
        if token.isalpha():
            token = str(input(f"Insert the value of {token}: "))

        if token.isdigit() or token.replace(".", "").isdigit():
            opStack.push(float(token))
        #test
        elif token == "~":
            operand1 = opStack.pop()
            result = domath(token, operand1)
            opStack.push(result)

        else:
            operand1 = opStack.pop()
            operand2 = opStack.pop()
            result = domath(token, operand1, operand2)
            opStack.push(result)

    if len(opStack.items) > 1:
        raise SyntaxError("Notation is not correct")

    return opStack.pop()


#################
# -- Testing -- #
#################

if __name__ == "__main__":

    infix = "[4&0]*-2"
    print(prefixEvaluation(infix))

# Two - char number (Sanad, works but spaces are broken)
# brackets inversion (done inline)
# gui (done ahmed adel)
