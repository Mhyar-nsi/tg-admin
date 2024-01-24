import os
from config import app
from hydrogram import filters
from models import *
from utils import *
from buttons import *



ADMIN = int(os.getenv('ADMIN'))
db = Model()

@app.on_message(filters.private & filters.command('start'))
async def start_handler(_, message):
    
    chat_id = message.chat.id
    message_id = message.id

    
    user = await db.check_user(chat_id=chat_id)
    
    if user is None:            
        await db.create_user(
            chat_id=chat_id,
            full_name=message.from_user.first_name,
            username=message.from_user.username
        )
    
    await app.send_message(
        chat_id=chat_id,
        text='Hi',
        reply_markup=HOME,
        reply_to_message_id=message_id
    )
    

@app.on_message()
async def send_to_admin(_, message):
    
    chat_id = message.chat.id
    user_message = message.text

    await app.send_message(
        chat_id=chat_id,
        text='Your message was send'
    )
    
    await app.send_message(
        chat_id=ADMIN,
        text=user_message,
        reply_markup=ANSWER
    )


if __name__ == '__main__':
    app.run()