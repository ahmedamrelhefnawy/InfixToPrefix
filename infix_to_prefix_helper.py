from ValidityChecker import isvalid
import re


def filter(astring):

    # this line replaces all negative numbers & brackets with a special char ~
    astring = re.sub(r"(([^\w\)\]\}\s]|^|\(\[\{) *)(\-)", r"\1~", astring)

    # this one adds a * between numbers and brackets for this syntax A(B+C)=>A*(B+C)
    astring = re.sub(r"(\w *)(\(\[\{)", r"\1*\2", astring)

    # this is  a regex that matches words and multi digit numbers
    # in addition to operators and decimals
    regex = r"\.\w+|\w+(?:\.\w+)?|[^\s\w]"

    # here we use the regex to return a list of all matches
    # while ignoring everything else(spaces,newlines,...etc)
    return re.findall(regex, astring)


def infix_to_prefix_helper(astring):
    '''A function that makes sure that the infix notation is valid and ready to be processed'''

    # Handling User Mistakes

    # Incorrectly typed brackets
    if not isvalid(astring):
        raise SyntaxError("Brackets are not typed correctly")

        # Separating Oprators and Operands
    stringlist = filter(astring) 

    return stringlist[::-1]

#################
# -- Testing -- #
#################


if __name__ == "__main__":
    print(filter("-2( --3)"))
