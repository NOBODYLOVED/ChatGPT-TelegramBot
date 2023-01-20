import openai
import telebot
from config import TOKEN, OpenAI_API

"""Connect tg, openai"""
openai.api_key = OpenAI_API
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я не очень хорошо работаю, '
                     'но могу тебя развлечь :)')


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    """Get-send openAI text messages"""
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.5,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]
                                                                ['text'])


if __name__ == "__main__":
    bot.polling()
