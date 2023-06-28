from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import openai,base64,telegram


def enc(message):return base64.b64encode(message.encode('ascii')).decode('ascii')
def dec(key):return base64.b64decode(key.encode('ascii')).decode('ascii')

DATABASE_FILE = "database.txt"
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
openai.api_key = 'YOUR_OPENAI_API_KEY'



def add(a, b):
    b = enc(b)
    data = f"{a.lower()}:{b}\n"
    with open(DATABASE_FILE, "a") as file:
        file.write(data)

def query(a):
    with open(DATABASE_FILE, "r") as file:
        for line in file:
            key, value = line.strip().split(":")
            if key.lower() == a.lower():
                return dec(value)
    return False


def create(word):
  q = query(word)
  if q == False:

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[

              {"role": "user", "content": f"""
  Define this word in a few easy words and write 2 short sentences using this word with easy words: {word} """},
          ]
  )

    result = ''
    for choice in response.choices:
        result += choice.message.content
    add(word,result)
    return result
  else: return q


def process_message(update, context):
    user_id = update.effective_chat.id
    word = update.message.text
    response = create(word)
    context.bot.send_message(chat_id=user_id, text=response
                ,  parse_mode=telegram.ParseMode.HTML)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
