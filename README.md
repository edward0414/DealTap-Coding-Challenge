# URL Shortener - DealTap Coding Challenge

### Set Up

Set up the environment by installing the packages in the requirements.txt file.
-> "pip install pymongo Flask requests" or "pip install -r requirements.txt"

Run the command "python app.py" in the command line. 

Then the server will be up and running on the localhost port 4000. 

   * Use virtualenv
   * Do not need to run db_create.py. The db is created already. 


### Specifications


### Database

It is a NoSQL database using MongoDB. Hosted on mlab.

Schema:

counters
- _id: String
- sequence_val: Integer

url
- id: Integer
- longURL: String
- shortURL: String
- requests: [
	request_id, 
	...
]

request
- shortURL: String
- ip: String,
- platform: String,
- browser: String,
- version: String,
- time: String
}


### Test

Similar to how to run the main app.py file, run the command "python test.py" to test the endpoints.

Test cover:
1) correct behaviour of /conversations endpoint
2) incorrect behaviour of /conversations endpoint
3) correct behaviour of /messages endpoint
4) incorrect behaviour of /messages endpoint
4) correct process of creating a new conversation


### Down the road

As the database gets bigger, I could implement data sharding to dael with scalibilty problems. 



