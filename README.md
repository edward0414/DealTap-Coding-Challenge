# DealTap Coding Challenge

### Set Up

Set up the environment by installing the packages in the requirements.txt file.
-> "pip install pymongo Flask" or "pip install -r requirements.txt"

Run the command "python app.py" in the command line. 

Then the server will be up and running on the localhost port 4000. 

   * Use virtualenv
   * Do not need to run db_create.py. The db is created already. 


### Specifications


### Database

It is a NoSQL database using MongoDB. Hosted on mlab.

Schema:

counter
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
- _id: given int
- url-id: Integer
- info: {
	ip: String,
	device: String,
	time: String
}


### Test

Similar to how to run the main app.py file, run the command "python test.py" to test the endpoints.

Test cover:



