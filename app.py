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
#-Post to /index longURL convert form
#	-> add the longURL to the collection URL (id, longURL, shortURL)
#	-> use the id (from auto-increment) to create a shortURL address
#	-> return a HTML page with the shortURL
#-Get to /shortURL/<shortURL>
#	-> record the request info (ip, device, time)
#	-> redirect to the longURL page by querying the db
#
#-Post to /index shortURL info form
#	-> query the stats of this link
#	-> redirect to the shortURL info page

class Converter:

	_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	_base = len(_letters)

	def convertToURL(self, num):

		result = ''

		while num > 0:

			remain = num // self._base
			dig = num % self._base
			num = remain
			result = self._letters[dig] + result

		return result

	def convertToNum(self, url):

		num = 0

		for char in url:
			num = num * self._base + self._letters.index(char)

		return num







if __name__ == "__main__":
	b = Converter()
	url = b.convertToURL(3)
	print url
	print b.convertToNum(url)

    #app.run(host='0.0.0.0',port=4000)
