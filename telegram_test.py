import time

import requests
import time
bot_token = "5466008742:AAHmyquxOhcDkPPMngLfYxL6KIvXgKnAQlI"

# Replace YOUR_CHAT_ID with the chat ID of the chat where you want to send the message
chat_id = "1687298484"

group_id = "-1001814728356"

# Replace YOUR_MESSAGE with the message you want to send
message = "Hello, group chat!"

# Make a request to the Telegram API to send the message
response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",
                         data={"chat_id": chat_id, "text": message})

# Print the response from the Telegram API
while True:
    print(response.json())
    time.sleep(2)
