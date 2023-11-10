def domath(operator, op1, op2=0):

    if operator == "+":
        return op1 + op2

    if operator == "-":
        return op1 - op2

    if operator == "*":
        return op1 * op2

    if operator == "^":
        return op1 ** op2

    if operator == "~":
        return 0 - op1

    if operator == "%" and op2 != 0:
        return op1 % op2

    if operator == "/" and op2 != 0:
        return op1 / op2

    if (operator == "/" or "%") and op2 == 0:
        raise SyntaxError("Division By Zero")
