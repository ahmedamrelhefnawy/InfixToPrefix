from stack import stack
from infix_to_prefix_helper import infix_to_prefix_helper


def infix_to_prefix(astring):

    prec = {}
    prec["~"] = 5
    prec["^"] = 4
    prec["%"] = 3
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["]"] = 1
    prec["}"] = 1
    prec[")"] = 1

    tokenlist = infix_to_prefix_helper(str(astring))
    prefixlist = []
    opstack = stack()

    for token in tokenlist:
        if token.isalpha() or token.replace(".", "").isdigit():
            prefixlist.append(token)

        elif token in ")}]":
            opstack.push(token)

        elif token in "({[]":
            while opstack.peek() not in "]})":
                prefixlist.append(opstack.pop())
            opstack.pop()

        else:  # operator
            while not opstack.isempty() and prec[opstack.peek()] > prec[token]:
                prefixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isempty():
        prefixlist.append(opstack.pop())

    return " ".join(prefixlist[::-1])


#################
# -- Testing -- #
#################

if __name__ == "__main__":

    # print(infix_to_prefix("A + ( C - D ^ 2 ) - { B }")) #True
    # print(infix_to_prefix("A + ( C - D ^ 2 ] - { B }")) #Different Bracket
    # print(infix_to_prefix("~A * B+ C * ~D")) #NotClosed Bracket
    print(infix_to_prefix("(5+3)*(4%2)-7^2"))
