from flask import Flask      #import flask class
app = Flask(__name__)        #make an instance of the class, passing the name as an argument - __name__

import json
import random
import nltk

@app.route('/hello')              #tells which URL should trigger the function
def hello_world():
	return 'hello world'

@app.route('/sentence')             
def showSentence():

	with open('pos_list.json') as f:
		pos_list = json.load(f)

	with open('sentences.json') as file:

		list_of_sentences = json.load(file)
		sentence = random.choice(list_of_sentences['sentences'])  # get a random sentence
		sentence.replace(',','')
		sentence.replace('.','')
		sentence.replace('?','')
		sentence.replace('!','')

		tokenizer = nltk.RegexpTokenizer(r"\w+")  # remove punctuation
		words = tokenizer.tokenize(sentence)	  # split sentence into words
  
		tagged_words = nltk.pos_tag(words)     # creates an array of tuples with (word, pos) for each

		for w in tagged_words:
			print(w)
		print(pos_list)

		html = ''
		spaces = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

		for w in tagged_words:
			word = w[0]
			pos_abbrev = w[1]

			pos = pos_list[pos_abbrev]
			html += word + spaces + pos + "<br><br>"

	return html

# set FLASK_APP=application.py
# flask run

#note: any changes I make won't be shown on refresh - I need to stop, then run flask again.