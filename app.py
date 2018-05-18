#use Flask framework
#use mongodb as Database
#set up the environment using anaconda
from flask import Flask, request, jsonify, json
from datetime import datetime
from pymongo import MongoClient

# create the application object
app = Flask(__name__)

#it would be a better idea to save the credentials as environmental secret keys for better security!
#but just for the person to run the code, i will leave it as this
client = MongoClient('mongodb://edward:123456@ds127490.mlab.com:27490/dealtap_challenge') 

db = client['dealtap_challenge']


#To-Do:
#-Counter
#	-> for auto-increment id
#-Post to /longURL (sender, conversation_id, message)
#	-> validating incoming data (check if its the right format)
#	-> insert to the db according to the conversation_id
#-Get to /conversations/<conversation_id>
#	-> validating incoming id
#	-> query the db

class Converter:

	_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	_base = len(_letters)

	def convertToURL(self, num):

		while num > 0:



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000)
