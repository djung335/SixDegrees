from tree import Tree
import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')


# given a subject, creates a Tree based on the wikipedia page's links

def treePopulator(subject, count, dupChecker):
    count = count + 1
    allLinks = wiki_wiki.page(subject).links
    listOfLinks = []

    if count == 6:
        return Tree(subject, listOfLinks)
    else:
        for title in allLinks.keys():
            if title not in dupChecker:
                listOfLinks.append(title)
                dupChecker.add(title)
            return Tree(subject, listConverter(listOfLinks, count, dupChecker))


def listConverter(listOfLinks, count, dupChecker):
    listOfTrees = []
    for title in listOfLinks:
        if title not in dupChecker:
            dupChecker.add(title)
            listOfTrees.append(treePopulator(title, count, dupChecker))
            return listOfTrees


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
    print(startNode.val)
    while queue:
        m = queue.pop(0)

        if m.val == finishNode:
            pathFinder(parentTracker, m.val)
            return list.reverse(path)

        for child in m.listOfChildren:
            if child.val not in visited:
                print(child.val)
                visited.append(child)
                queue.append(child)
                parentTracker[child.val] = m.val


def pathFinder(parentTracker, child):
    while parentTracker[child] != None:
        path.append(parentTracker[child])
        child = parentTracker[child]
