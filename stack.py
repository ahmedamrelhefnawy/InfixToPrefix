class stack:
    ''' stack class'''

    def __init__(self):
        '''stack object initialization'''
        self.items = []

    def size(self):
        '''size of stack object'''
        return len(self.items)

    def isempty(self):
        '''checks if stack object is empty'''
        return len(self.items) == 0

    def pop(self):
        '''gets and removes the last item of the stack object'''
        return self.items.pop()

    def push(self, item):
        '''adds new item to the top of the stack object'''
        self.items.append(item)

    def peek(self):
        '''reads the last item in the stack'''
        return self.items[-1]
