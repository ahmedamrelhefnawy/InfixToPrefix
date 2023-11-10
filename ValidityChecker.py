from stack import stack


def isvalid(astring):
    s = stack()
    for token in astring:
        if token in "{[(":
            s.push(token)
        elif token in "}])":
            if s.isempty():
                return False
            else:
                left = s.pop()
                if (token == "}" and left != "{") or \
                    (token == "]" and left != "[") or \
                        (token == ")" and left != "("):
                    return False
    return s.isempty()
