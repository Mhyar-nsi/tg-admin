from config import app
from hydrogram import filters
from utils import *
import os


ADMIN = int(os.getenv('ADMIN'))

@app.on_message(filters.private & filters.command('start'))
async def start_handler(_, message):
    
    chat_id = message.chat.id
    message_id = message.id
    
    await app.send_message(
        chat_id=chat_id,
        text='Hi',
        reply_to_message_id=message_id
    )
    
    await app.send_message(
        chat_id=ADMIN,
        text=f'{chat_id}'
    )
    
    
@app.on_message(filters.private & filters.command('yt'))
async def youtube_handler(_, message):
    
    chat_id = message.chat.id
    message_id = message.id
    
    url = message.command[1]   
    
if __name__ == '__main__':
    app.run()