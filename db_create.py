# start counter

from app import db

db.createCollection("counters")

db.counters.insert({_id:"URLid",sequence_value:0})
