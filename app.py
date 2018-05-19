#use Flask framework
#use mongodb as Database
#set up the environment using anaconda
from flask import Flask, request, jsonify, json, redirect, render_template, url_for
from datetime import datetime
from pymongo import MongoClient, ReturnDocument
import requests

# create the application object
app = Flask(__name__)

#it would be a better idea to save the credentials as environmental secret keys for better security!
#but just for the person to run the code, i will leave it as this
client = MongoClient('mongodb://edward:123456@ds127490.mlab.com:27490/dealtap_challenge') 

db = client['dealtap_challenge']


#To-Do:
#-Counter
#	-> for auto-increment id
#-Converter
#   -> convert num -> URL, URL -> num
#-Post to /index longURL convert form
#	-> add the longURL to the collection URL (id, longURL, shortURL)
#	-> use the id (from auto-increment) to create a shortURL address
#	-> return a HTML page with the shortURL
#-Get to /shortURL/<shortURL>
#	-> record the request info (ip, device, time)
#	-> redirect to the longURL page by querying the db
#
#-Get to /info/<shortURL>
#	-> query the stats of this link
#	-> return a HTML page with the info

def getNextSequenceValue(sequenceName):
    
    query = {'_id': sequenceName}
    table = db['counters']
    update = {'$inc':{'sequence_value':1}}

    result = table.find_one_and_update(query, update, return_document=ReturnDocument.AFTER)

    return result['sequence_value']


def urlValidator(url):
    #a url validator that checks if the given url gives back http status code of 2XX
    #Not the best one but this will do...
    try: 
        resp = requests.get(url)
        print resp.status_code
    
        if str(resp.status_code)[0] != '2':
            return False
        else:
            return True
    
    except:
        return False

class Converter:
    """
    A converter that generates a short url using the _id of the document in the db.
    Idea:
    - Every time a long url is received, an auto-incremented id will be assigned to that long url.
    - Then, with that id, use this converter to convert the number to a short string that represents 
    the short url.
    - Together, this id, the long url, and the short url will be saved into the db as a document.
    """
    
	_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	_base = len(_letters)

	def convertToURL(self, num):
        #convert this 10-based number to 62-based number
        #then, use the letter to represent the 62-based number

		result = ''

		while num > 0:

			remain = num // self._base
			dig = num % self._base
			num = remain
			result = self._letters[dig] + result

		return result

	def convertToNum(self, url):
        #decode the url into a 62-based number
        #then, convert it back to 10-based number (the id in the db)

		num = 0

		for char in url:
			num = num * self._base + self._letters.index(char)

		return num
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    
    error = None
    shortURL = None

    if request.method == 'POST':
        longURL = request.form['longURL']

        #check if the url is valid
        if not urlValidator(longURL):
            error = "This URL does not seem valid. Perhaps you forgot to add http/https in front of it?"
            return render_template('index.html', error=error, shortURL=shortURL)

        table = db['url']

        result = table.find_one({"longURL": longURL})

        if result is None:
            seq = getNextSequenceValue('URLid')

            converter = Converter()
            shortURL = converter.convertToURL(seq)

            query = {
                '_id': seq,
                'longURL': longURL,
                'shortURL': shortURL
            }
            table.insert_one(query)
            
            shortURL = '/short/' + shortURL

        else:
            error = 'This long URL exists in the database already! Here is the shorten URL: ' + url_for('short', shortURL=result['shortURL'])

    return render_template('index.html', error=error, shortURL=shortURL)

@app.route('/short/<shortURL>')
def short(shortURL):
    
    #record the info about the user
    info = request.user_agent
    
    query = {
        'shortURL': shortURL,
        'ip_addr': request.remote_addr,
        'platform': info.platform,
        'browser': info.browser,
        'version': info.version,
        'time': datetime.utcnow()
    }
    
    table = db['url']
    
    result = table.find_one({'shortURL': shortURL})
    
    if result is not None:
        db['info'].insert_one(query)
        return redirect(result['longURL'])
    
    else:
        error = 'Invalid shortURL is entered.'
        shortURL = None
        
        return render_template('index.html', error=error, shortURL=shortURL)

@app.route('/info/<shortURL>')
def info(shortURL):
    info = None
    error = None
    
    query = {'shortURL': shortURL}
    
    result = db['info'].find(query)
    
    print "count:", result.count()
    
    if result.count() == 0:
        error = 'Invalud shortURL entered.'
    
    else:
        info = result
        
    return render_template('info.html', error=error, info=info)
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000)
