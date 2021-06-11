from flask import Flask, request, redirect, url_for, render_template
from urllib.request import urlopen as uReq
import wikipediaapi
from algorithm import *
from tree import Tree

wiki_wiki = wikipediaapi.Wikipedia('en')


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        # request.form comes in as a dictionary, so you can accesss each object using a key
        subjectOne = request.form["Subject One"]
        subjectTwo = request.form["Subject Two"]

       # convert each subject into a wikipedia page
        pageOne = wiki_wiki.page(subjectOne)
        pageTwo = wiki_wiki.page(subjectTwo)
        if pageOne.exists() and pageTwo.exists():
            return redirect('/connection/{}/{}'.format(subjectOne, subjectTwo))
        else:
            return "try again"


@app.route('/connection/<subjectOne>/<subjectTwo>')
def connection_page(subjectOne, subjectTwo):
    # path = bfs([], [], treePopulator(subjectOne, 0, set()), subjectTwo)
    wikiTree = treePopulator(subjectOne, 0, set())
    for child in wikiTree.listOfChildren:
        print(child.val)
    return "hello"