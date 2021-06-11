# A custom data structure to represent the connections that a wikipedia page
# has to its links
class Tree:
    def __init__(self, val, listOfChildren=[]):
        self.val = val
        self.listOfChildren = listOfChildren
