import tweepy
import webbrowser
import time

consumer_key = "3rJOl1ODzm9yZy63FACdg"
consumer_secret = "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8"

callback_uri = "oob"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)

webbrowser.open(redirect_url)

verifier = input("Enter the verification code: ")
auth.get_access_token(verifier)


print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
user = api.verify_credentials()
print(user.screen_name)

