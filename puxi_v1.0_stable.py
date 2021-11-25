import discord
import requests
import json
import random
from sad_words_list import list_sad_words
from encouragement_words import enc_words

client = discord.Client()


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg == client.user:
        return

    if message.channel.name == 'idei_bot':

        if msg.startswith('citat'):
            quote = get_quote()
            await message.channel.send(quote)

        # if any(word in msg for word in sad_words):
        for word in msg.split():
            if word.lower() in list_sad_words:
                await message.channel.send(random.choice(enc_words))

        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if message.author == client.user:
            return

        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'Acesta este numarul random: {random.randrange(1000000)} !'
            await message.channel.send(response)
            return

        if user_message.lower() == '!anywhere':
            await message.channel.send('Aceasta chemare poate fi folosita global!')
            return


client.run('bot_token')



