from app import app
from flask import json, jsonify
from random import randint 
import unittest
from app import Converter


class FlaskTestCase(unittest.TestCase):
    
    def converter_test_1(self):
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
        
    
    def test_index_correct(self):
        tester = app.test_client(self)
        resp = tester.get('/')
        assert b'<h1>Short URL Generator</h1>' in resp.data
        assert b'<input type="longURL" placeholder="Long URL" name="longURL" class="input" required autofocus>' in resp.data
        assert b'<input class="btn" type="submit" value="Shorten">' in resp.data
#        resp = tester.post('/', data=dict(
#            longURL=''
#        ))
#
#	#Test conversations endpoint correct behaviour
#	def test_conversations_correct(self):
#		tester = app.test_client(self)
#		resp = tester.get('/conversations/1234') # I have written a sample conversation with this id in the db.
#		self.assertEqual(resp.status_code, 200)
#		data = json.loads(resp.data)
#		self.assertEqual(data['id'], '1234')
#
#	#Test conversations endpoint incorrect behaviour
#	def test_conversations_incorrect(self):
#		tester = app.test_client(self)
#		resp = tester.get('/conversations/234') # This conversation_id has not been used.
#		self.assertEqual(resp.status_code, 404)
#		data = json.loads(resp.data)
#		self.assertEqual(data['id'], '234')
#		self.assertEqual(data['messages'], "Error: No conversation has started with this id!")
#
#
#	#Test messages endpoint correct behaviour
#	def test_messages_correct(self):
#		tester = app.test_client(self)
#		req = {"conversation_id": "1234","message": "knock knock!", "sender": "edward"}
#		resp = tester.post('/messages', data=json.dumps(req), content_type='application/json')
#		data = json.loads(resp.data)
#		self.assertEqual(resp.status_code, 201)
#		self.assertTrue(data['successful'])
#		self.assertEqual(data['message']["sender"], "edward")
#		self.assertEqual(data['message']["message"], "knock knock!")
#
#
#	#Test messages endpoint incorrect behaviour
#	def test_messages_incorrect(self):
#		tester = app.test_client(self)
#		req = {"conversation_id": "1234", "sender": "edward"}
#		resp = tester.post('/messages', data=json.dumps(req), content_type='application/json')
#		self.assertEqual(resp.status_code, 400)
#		data = json.loads(resp.data)
#		self.assertEqual(data["successful"], False)
#
#	#Test the process of creating a new conversation
#	def test_new_conversation(self):
#		tester = app.test_client(self)
#
#		#start a new conversation
#		x = randint(1, 9999) #theres a good chance this id hasnt been used
#		x = str(x)
#		req = {"conversation_id": x,"message": "Hello ShiHan!", "sender": "Edward"}
#		resp = tester.post('/messages', data=json.dumps(req), content_type='application/json')
#		data = json.loads(resp.data)
#		self.assertEqual(resp.status_code, 201)
#		self.assertTrue(data['successful'])
#		self.assertEqual(data['message']["sender"], "Edward")
#		self.assertEqual(data['message']["message"], "Hello ShiHan!")
#
#		#check the log for that conversation
#		resp2 = tester.get('/conversations/' + x)
#		data2 = json.loads(resp2.data)
#		self.assertEqual(resp2.status_code, 200)
#		self.assertEqual(data2['id'], x)
#		self.assertEqual(data2['messages'][0]["sender"], "Edward")
#		self.assertEqual(data2['messages'][0]["message"], "Hello ShiHan!")


if __name__ == "__main__":
	unittest.main()