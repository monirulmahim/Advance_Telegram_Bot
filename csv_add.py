import APIs
import telebot
import csv

API_KEY = APIs.token
bot = telebot.TeleBot(API_KEY)

def csv_file(ids, name):
	while True:
		with open('chat_ids.csv', 'r', newline='') as csvfile:
			csvreader = csv.reader(csvfile)
			chat_id = [int(row[0]) for row in csvreader]
			
		if ids not in chat_id:
			chat_id.append(ids)
			print(f"{ids} {name} Added")
			with open('chat_ids.csv', 'a', newline='') as csvfile:
				csvwriter = csv.writer(csvfile)
				csvwriter.writerow([ids, name])
				break
		else:
			return False


def remove_item_csv(chatid):
	with open('chat_ids.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		rows = list(csvreader)
	for i in rows:
		ids = i[0]
		if ids == chatid:
			index = rows.index(i)
			rows.pop(index)
			print('ID removed from CSV file')
			break
	with open('chat_ids.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(rows)



@bot.message_handler(commands=['start', 'help', 'add', 'remove'])
def send_welcome(message=None):
	if message.text ==  '/start':
		bot.reply_to(message, "Hello! To add yourself on Best Motivational Islamic Quotes, simply type /add")


	elif message.text ==  '/add':
		chat_id = message.chat.id
		name = message.chat.first_name
		if csv_file(chat_id,name) != False:
			bot.reply_to(message, f"You're Successfully added Now! If You want to remove just type /remove Your {chat_id}")
		else:
			bot.reply_to(message, f"You're Already added! If You want to remove just type /remove {chat_id}")


	elif message.text ==  '/remove':
		chat_id = f"{message.chat.id}"
		remove_item_csv(chat_id)
		print(chat_id)
		bot.reply_to(message, "You're Successfully removed!")	


	else:
		name('help')
		bot.reply_to(message, 'help')
	

bot.polling()





		

