from app import app
from flask import url_for
import unittest
from util import Converter
import requests

def parseURL(string):
    
    target = 'This long URL exists in the database already! Here is the shorten URL: /short/'
    
    ind = string.index(target) + len(target)
    
    result = ''
    
    while string[ind] != '<':
        result += string[ind]
        ind += 1
        
    return result


class FlaskTestCase(unittest.TestCase):
    
    def test_index_get(self):
        tester = app.test_client(self)
        resp = tester.get('/')
        assert b'<h1>Short URL Generator</h1>' in resp.data
        assert b'<input type="longURL" placeholder="Long URL" name="longURL" class="input" required autofocus>' in resp.data
        assert b'<input class="btn" type="submit" value="Shorten">' in resp.data
    
    def test_index_exist(self):
        tester = app.test_client(self)
        
        #post an url that exists in the db
        resp = tester.post('/', data=dict(
            longURL='https://conda.io/docs/_downloads/conda-cheatsheet.pdf'
        ))
        assert b'This long URL exists in the database already!' in resp.data

    def test_index_invalid_url(self):
        tester = app.test_client(self)
        resp = tester.post('/', data=dict(
            longURL='happy.e'
        ))
        assert b'This URL does not seem valid. Perhaps you forgot to add http/https in front of it?' in resp.data 
        
    def test_short_get_exist(self):
        tester = app.test_client(self)
        resp = tester.get('/short/b') #espn.com
        
        self.assertEqual(resp.location, 'http://www.espn.com/')

    def test_short_get_invalid(self):
        tester = app.test_client(self)
        resp = tester.get('/short/a') #invalid shortURL that is not in the db
        assert b'Invalid shortURL is entered.' in resp.data
        
    def test_info_get_exist(self):
        tester = app.test_client(self)
        resp = tester.get('/info/b') #exist in the db
        assert b'<th>IP</th>' in resp.data #the table appears
        assert b'<th>Platform</th>' in resp.data
        assert b'<th>Browser</th>' in resp.data
        assert b'<th>Version</th>' in resp.data
        
    def test_info_get_invalid(self):
        tester = app.test_client(self)
        resp = tester.get('/info/a') #invalid shortURL that is not in the db
        assert b'<strong>Error:</strong>' in resp.data
        
    def test_existing_long_url(self):
        tester = app.test_client(self)
        resp = tester.post('/', data=dict(
            longURL='https://github.com/edward0414'
        ))
        assert b'This long URL exists in the database already!' in resp.data
        
        shortURL = parseURL(resp.data)
        
        print "url:", shortURL
        
        resp = tester.get('/short/' + shortURL)
        self.assertEqual(resp.location, 'https://github.com/edward0414')
        
        r = requests.get(url_for('short', shortURL=shortURL, _external=False))
        
        resp = tester.get('/info/' + shortURL) #exist in the db
        assert b'<th>IP</th>' in resp.data #the table appears
        assert b'<th>Platform</th>' in resp.data
        assert b'<th>Browser</th>' in resp.data
        assert b'<th>Version</th>' in resp.data
        

if __name__ == "__main__":
	unittest.main()