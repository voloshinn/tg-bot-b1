from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery as cq
from aiogram.filters import CommandStart, Command

import text
import app.kb as kb
import config

router = Router()




@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('SELECT LANGUAGE 👅⬇️',
    reply_markup=kb.select_language)




@router.callback_query(F.data == 'english')
async def english(callback: cq):
    await callback.answer('')
    selected_language = 'english'
    await callback.message.answer(text.HELLO[selected_language], reply_markup=kb.start)

@router.callback_query(F.data == 'russian')
async def russian(callback: cq):
    await callback.answer('')
    selected_language = 'russian'
    await callback.message.answer(text.HELLO[selected_language], reply_markup=kb.start)

@router.callback_query(F.data == 'hindi')
async def hindi(callback: cq):
    await callback.answer('')
    selected_language = 'hindi'
    await callback.message.answer(text.HELLO[selected_language], reply_markup=kb.start)
    