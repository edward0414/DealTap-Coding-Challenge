from app import app
from flask import url_for
from random import randint 
import unittest
from util import Converter


class FlaskTestCase(unittest.TestCase):
    
    def test_index_get(self):
        print "there"
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
        self.assertEqual(resp.status_code, 302)
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
        
    def converter_test_1(self):
        print "here"
        conv = Converter()
        i = 0
        while i < 10:
            x = randint(1, 9999)
            short = conv.converToURL(x)
            num = conv.converToNum(short)
            print num == x
            assert num == x
            i += 1
            
    def converter_test_2(self):
        conv = Converter()
        assert 'bb' == conv.convertToURL(63)
        assert 'ba' == conv.convertToURL(62)
        assert '9' == conv.convertToURL(61)

if __name__ == "__main__":
	unittest.main()