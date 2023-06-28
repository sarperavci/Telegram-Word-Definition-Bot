# Telegram Word Definition Bot

This is a Telegram bot that retrieves the definition and example sentences of a given word using the OpenAI ChatGPT API. The bot interacts with users on Telegram and provides them with the requested information.

## Prerequisites

Before running the bot, make sure you have the following requirements installed:

- Python 3.7 or higher
- `telegram` library (`python-telegram-bot`)
- `openai` library (`openai`)

You can install the required libraries using `pip`:

```bash
pip install python-telegram-bot openai
```

## Setup

To set up the Telegram bot and integrate it with the OpenAI ChatGPT API, follow these steps:

1. Create a new bot on Telegram by talking to the [BotFather](https://core.telegram.org/bots#6-botfather).
2. Obtain the Telegram API token for your bot.
3. Create an OpenAI account if you haven't already.
4. Generate an OpenAI API key and make sure it has access to the ChatGPT API.

## Configuration

Open the `main.py` file and update the following variables with your configuration:

```python
DATABASE_FILE = "database.txt"
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

Make sure to replace `'YOUR_TELEGRAM_BOT_TOKEN'` with the Telegram API token you obtained earlier and `'YOUR_OPENAI_API_KEY'` with your OpenAI API key.

## Usage

To use the Telegram bot, follow these steps:

1. Start the bot by running the `main.py` script:

   ```bash
   python main.py
   ```

2. Start a conversation with your bot on Telegram.

3. Send a word to the bot, and it will respond with the definition and two example sentences for that word.

## Data Storage

The bot uses a simple text file (`database.txt`) to store previously requested word definitions. When a user requests the definition of a word, the bot checks if the definition is already present in the file. If it exists, it retrieves the definition from the file. Otherwise, it uses the OpenAI ChatGPT API to generate the definition and saves it in the file for future use.

## API Usage and Cost

The OpenAI ChatGPT API has usage limits and costs associated with it. The current cost per query for this API is 0.00015 USD. Make sure to review the OpenAI pricing and usage details to understand any potential charges.

## Inspiration and More Information

The idea for this Telegram bot comes from [Sarper Avci's website](https://sarperavci.com/i-transformed-my-raspberry-pi-into-an-enhanced-english-dictionary-server/). You can find more information and details about the project on the website.

## License

This project is licensed under the [MIT License](LICENSE).
