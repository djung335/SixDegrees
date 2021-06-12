from tree import Tree
import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')


# given a subject, creates a Tree based on the wikipedia page's links
def treePopulator(subject, dupChecker):
    # generates all the links based on the given subject in the form of a list
    allLinks = wiki_wiki.page(subject).links
    # creates the initial
    sixDegreesTree = Tree(subject)
    for title in allLinks.keys():
        if title not in dupChecker:
            sixDegreesTree.addChild(Tree(title))
            dupChecker.add(title)
    for child in sixDegreesTree.listOfChildren:
        if child.getLevel() != None and child.getLevel() <= 6:
            child.treePopulator(title, dupChecker)
    return sixDegreesTree


# represents the list of visited nodes in the tree.
visited = []
# a queue for my implementation of breadth-first search.
queue = []
# represents the path from one subject to another.
path = []
# represents a dictionary to map child nodes to their parents.
parentTracker = {}


def bfs(visited, queue, startNode, finishNode):
    visited.append(startNode)
    queue.append(startNode)

    while queue:
        m = queue.pop(0)

        if m.val == finishNode:
            while m.parent != None:
                path.append(m.val)
                m = m.parent
            return list.reverse(path)

        for child in m.listOfChildren:
            if child.val not in visited:
                visited.append(child)
                queue.append(child)
                parentTracker[child.val] = m.val
