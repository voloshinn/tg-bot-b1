from aiogram.types import (
  ReplyKeyboardMarkup,
  KeyboardButton,
  InlineKeyboardMarkup,
  InlineKeyboardButton,
)

import text
import config

start = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text=text.AFTER_START['hindi'])],
],
  resize_keyboard=True,
  input_field_placeholder='Select language')



select_language = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='🌐 English', callback_data='english')],
  [InlineKeyboardButton(text='🇮🇳 हिन्दी', callback_data='hindi')],
  [InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian')],
],
  resize_keyboard=True,
  input_field_placeholder='Select language')



