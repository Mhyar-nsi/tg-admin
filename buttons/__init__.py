from hydrogram.types import (
    ReplyKeyboardMarkup, 
    InlineKeyboardMarkup, 
    KeyboardButton, 
    InlineKeyboardButton, 
    ReplyKeyboardRemove
)


HOME = ReplyKeyboardMarkup(
    [
        ['👤 درباره من']
    ],
    resize_keyboard=True, 
    one_time_keyboard=True 
)

ANSWER = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text='پاسخ به یوزر', 
                callback_data='answer'
            )
        ],
    ]
)

CANCEL = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text='لغو', 
                callback_data='cansel'
            )
        ],
    ]
)