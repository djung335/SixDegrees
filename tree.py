# This class is a tree data structure.
class Tree:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.listOfChildren = []

# A method to add a child to a tree.
    def addChild(self, child):
        self.listOfChildren.append(child)
        child.parent = self

# A method to print the Tree.
    def printTree(self):
        spaces = ' ' * (self.getLevel() * 3)
        print(spaces + self.val)  # make this spaces + self.val
        # this if statement is to check if the listOfChildren has elements or not.
        if self.listOfChildren:
            for child in self.listOfChildren:
                child.printTree()

# A method to get the level of a Tree.
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent
        return level
