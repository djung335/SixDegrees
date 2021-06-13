from tree import Tree
import wikipediaapi
import random

wiki_wiki = wikipediaapi.Wikipedia('en')

# given a subject, creates a Tree based on the wikipedia page's links


def treePopulator(root):
    # generates all the links based on the given subject in the form of a list
    links = wiki_wiki.page(root.val).links.keys()

    threeLinks = random.sample(links, min(3, len(links)))
    if root.getLevel() <= 4:
        addAllChildren(root, threeLinks)
        for child in root.listOfChildren:
            treePopulator(child)


def addAllChildren(parentTree, links):
    for title in links:
        parentTree.addChild(Tree(title))


def shortestPathFinder(root, subject):
    ret = []
    connection = []
    pathFinder(root, subject, ret, connection)
    index = findIndexOfShortestList(ret)
    if index == -1:
        return ["no path!"]
    else:
        return ret[index]


def pathFinder(root, subject, ret, connection):
    if root is None:
        return
    connection.append(root.val)
    if root.val == subject:
        ret.add(list.copy(connection))

    for child in root.listOfChildren:
        pathFinder(child, subject, ret, connection)

    connection.pop()


def findIndexOfShortestList(ret):
    # sizes = []
    # for list in ret:
    #     sizes.append(len(list))

    sizes = [len(list) for list in ret]
    if len(sizes) == 0:
        return -1
    else:
        smallestSize = min(sizes)
        return sizes.index(smallestSize)
