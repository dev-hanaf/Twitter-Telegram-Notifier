import tweepy
import time
import requests

# Your Twitter API keys
consumer_key = "3rJOl1ODzm9yZy63FACdg"
consumer_secret = "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8"

access_token = "1642419603375632386-H67E7y593bR8l9c88rrkprZiTvb30b"
access_token_secret = "y8IDHUJcACt7YyOOG6JFcIx01iETo6q1qulWG4QKLazmH"

# Authenticate with the Twitter API using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# The screen name of the user you want to check for new tweets
user_screen_name = "1337FIL"

# Initialize the last tweet ID to 0
last_tweet_id = 0

while True:
    # Get the user's timeline (most recent tweets) with Tweepy
    timeline = api.user_timeline(screen_name=user_screen_name, count=1)

    # If the timeline is not empty and the tweet ID is different than the previous one
    if timeline and timeline[0].id != last_tweet_id:
        # Save the new tweet ID
        last_tweet_id = timeline[0].id

        # Do something with the new tweet, for example print its text
        print("New tweet from {}: {}".format(user_screen_name, timeline[0].text))
        # Replace YOUR_TOKEN with your actual bot token
        bot_token = "5466008742:AAHmyquxOhcDkPPMngLfYxL6KIvXgKnAQlI"

        # Replace YOUR_CHAT_ID with the chat ID of the chat where you want to send the message
        chat_id = "1687298484"

        group_id = "-1001814728356"

        # Replace YOUR_MESSAGE with the message you want to send
        messageTel = "https://candidature.1337.ma/meetings"

        # Make a request to the Telegram API to send the message
        num_messages = 10

        for i in range(num_messages):
            response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",
                                     data={"chat_id": group_id, "text": messageTel})

            print(response.json())
            time.sleep(2)

    # Wait for 5s before checking for new tweets again
    time.sleep(5)
