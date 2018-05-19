# URL Shortener - DealTap Coding Challenge

### Set Up

Set up the environment by installing the packages in the requirements.txt file.
-> "pip install pymongo Flask requests" or "pip install -r requirements.txt"

Run the command "python app.py" in the command line. 

Then the server will be up and running on the localhost port 4000. 

   * Use virtualenv
   * Do not need to run db_create.py. The db is created already. 


### Specifications

   * `/` - where you can enter a long url into the form and generate a short url
   * `/short/<shortURL>` - where you use the shorten url and it redirects to its original url
   * `/info/<shortURL>` - where you see a list of info about users who have used the shorten url

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
1) GET method on `/`
2) POST existing longURL on `/`
3) POST invalid longURL on `/`
4) GET existing shortURL on `/short/<shortURL>`
5) GET invalid shortURL on `/short/<shortURL>`
6) GET existing shortURL on `/info/<shortURL>`
7) GET invalid shortURL on `/info/<shortURL>`
8) A whole process of utilizing `/`, `/short/<shortURL>`, and `/info/<shortURL>`



### Down the road

As the database gets bigger, I could implement data sharding to dael with scalibilty problems. 



