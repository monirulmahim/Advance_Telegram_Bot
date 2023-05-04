import APIs
import random
import requests
import csv
import json
from time import sleep



bot_token = APIs.token
telegram_url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
message = "ITS a TEST!"

while True:
	with open('chat_ids.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		rows = list(reader)

	for i in rows:
		chat_id  = i[0]
		payload = {
			"chat_id": chat_id,
			"text": message
			}

		response = requests.post(telegram_url, data=payload)

		# Print the response from the Telegram API
		print(json.loads(response.content))
	sleep(10)
