# start counter

from app import db

db.create_collection('counters')

table = db['counters']

table.insert_one({'_id':"URLid",'sequence_value':0})
