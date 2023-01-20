import openai
import telebot   # don't know how to solve, weird mypy problem
from config import TOKEN, OpenAI_API

"""Connect tg, openai"""
openai.api_key = OpenAI_API
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    """Prepared answer for /start."""
    bot.send_message(message.chat.id, 'Привет, я не очень хорошо работаю, '
                     'но могу тебя развлечь :)')


@bot.message_handler(func=lambda _: True)  # _ to ignore
def handle_message(message):
    """Get-send openAI text messages"""
    response = openai.Completion.create(
        model='text-davinci-003',  # Can change variety, check OpenAI
                                   # playground.
        prompt=message.text,
        temperature=0.5,  # control randomness, means less = less random.
                          # More = more random.
        max_tokens=3000,  # max symbols in answer
        top_p=1.0,  # probability mass. Change for less probability answers
        frequency_penalty=0.5,   # chance to get same answer
                                 # in the answer chain.
        presence_penalty=0.0,       # chance to get exactly same answer.
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]
                                                                ['text'])
    # Fitering correct answer


if __name__ == "__main__":
    """Good code."""
    bot.polling()
