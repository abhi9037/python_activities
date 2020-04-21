from user import User
from database import Database
from twitter_utils import *

Database.initialise(user='postgres', password= '1234', database='learning',host='localhost')

email = input("Enter email id: ")
user = User.load_from_db_by_email(email)
if not user:
    request_token = get_request_token()
    verifier = get_oauth_verifier(request_token)
    access_token = get_access_token(request_token,verifier)

    print(access_token)

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    user = User(email,first_name,last_name, access_token['oauth_token'], access_token['oauth_token_secret'],None)
    user.save_to_db()


tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])