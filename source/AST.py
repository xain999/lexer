class AST:

    booleans = ['True', 'TRUE', 'true', 'False', 'FALSE', 'false']

    def __init__(self, l, r, v):
        self.left = l
        self.right = r
        self.value = v

    def tautology(self, mySet = ([]), myDict = {}):
        if len(mySet) == 0:
            return self.solve(myDict)

        ele = mySet.pop()

        myDict[ele] = True
        if not self.tautology(mySet, myDict):
            return False

        myDict[ele] = False
        return self.tautology(mySet, myDict)

    def unsatisfiable(self, mySet = ([]), myDict = {}):
        return not self.satisfiable(mySet, myDict)

    def satisfiable(self, mySet = ([]), myDict = {}):
        if len(mySet) == 0:
            return self.solve(myDict)

        ele = mySet.pop()

        myDict[ele] = True
        if self.satisfiable(mySet, myDict):
            return True

        myDict[ele] = False
        return self.tautology(mySet, myDict)

    def solve(self, myDict = {}):
        if self.right is None:
            return myDict[self.value]

        if self.value == '/\\':
            return self.left.solve(myDict) and self.right.solve(myDict)

        if self.value == '~':
            return not self.right.solve(myDict)

        if self.value == '\\/':
            return self.left.solve(myDict) or self.right.solve(myDict)

        if self.value == '==>':
            return self.imp(self.left.solve(myDict), self.right.solve(myDict))

        if self.value == '<=>':
            return self.iff(self.left.solve(myDict), self.right.solve(myDict))

    def findVariables(self, mySet = ([])):
        if self.right is None and self.value not in AST.booleans:
            return mySet.add(self.value)

        if self.left is not None:
            self.left.findVariables(mySet)

        if self.right is not None:
            self.right.findVariables(mySet)

        return mySet

    #solving BiConditional
    def iff(self, a, b):
        return self.imp(a, b) and self.imp(b, a)

    #solving Implication
    def imp(self, a, b):
        return (not a) or b

    #Just to display
    def prettyPrint(self):
        if self.left is not None and self.right is not None:
            return '(' + self.left.prettyPrint() + self.value + self.right.prettyPrint() + ')'

        if self.right is not None:
            return '(' + self.value + self.right.prettyPrint() + ')'

        return self.value

