#import makeWords

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Sky!'

'''
@app.route('/make/<word>')
def show_make(word):
    return repr(makeWords.wordToElems(word))
'''
