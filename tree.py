# A custom data structure to represent the connections that a wikipedia page
# has to its links
class Tree:
    def __init__(self, val, listOfChildren=None):
        self.val = val
        self.parent = None
        if listOfChildren is None:
            self.listOfChildren = []
        else:
            self.listOfChildren = listOfChildren

# A method to add a child to a tree.
    def addChild(self, child):
        self.listOfChildren.append(child)
        child.parent = self

# A method to print the Tree.
    def printTree(self):
        # spaces = ' ' * self.getLevel() * 3
        print(self.val)  # make this spaces + self.val
        # this if statement is to check if the listOfChildren has elements or not.
        if self.listOfChildren:
            for child in self.listOfChildren:
                child.printTree()

# A method to get the level of a Tree.
    def getLevel(self):
        level = 0
        p = self.parent
        while p != None:
            level = level + 1
            p = p.parent
