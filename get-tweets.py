import tweepy
username = '1337FIL'

# Enter your Twitter API credentials
consumer_key = "3rJOl1ODzm9yZy63FACdg"
consumer_secret = "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8"
access_token = "1642419603375632386-H67E7y593bR8l9c88rrkprZiTvb30b"
access_token_secret = "y8IDHUJcACt7YyOOG6JFcIx01iETo6q1qulWG4QKLazmH"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Enter the Twitter username of the user you want to search

# Collect tweets
tweets = []
new_tweets = api.user_timeline(screen_name=username, count=200, include_rts=False, tweet_mode='extended')
tweets.extend(new_tweets)
oldest_tweet_id = tweets[-1].id - 1

# Retrieve more tweets
while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=username, count=200, include_rts=False, tweet_mode='extended', max_id=oldest_tweet_id)
    tweets.extend(new_tweets)
    oldest_tweet_id = tweets[-1].id - 1

# Filter tweets that contain the phrase "check-in" and have at least one image
filtered_tweets = [tweet for tweet in tweets if 'piscine' in tweet.full_text.lower() and 'media' in tweet.entities]

# Display the filtered tweets with a good view
for tweet in filtered_tweets:
    print('Tweet ID:', tweet.id_str)
    print('Text:', tweet.full_text)
    print('Date:', tweet.created_at)
    print('Number of Images:', len(tweet.entities["media"]))
    print('Images:')
    for i, media in enumerate(tweet.entities["media"]):
        print(f'{i+1}. {media["media_url_https"]}')
    print('-'*50,'*')