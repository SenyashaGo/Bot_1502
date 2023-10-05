import asyncio
import telegram
import logging
import pandas as pd
import os
from aiogram import Bot, types
from aiogram.utils.markdown import text, bold, italic, code, pre, hitalic, escape_md, _join, hbold, hcode, hpre, \
    underline, hunderline, strikethrough, hstrikethrough, link, hlink, hide_link
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
import logging
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from config import BOT_TOKEN
import aiogram.utils.markdown as fmt

A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
     'w', 'x', 'y', 'z']

B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
     'W', 'X', 'Y', 'Z']

C = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
     'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']

D = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
     'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
     'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']

E = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Q = ['!', '@', '#', '$', '%', '&', '?', '-', '+', '=', '~']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

admin_chat_id = -1001678786017

cancel_button = KeyboardButton("Отмена")
cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_keyboard.add(cancel_button)


@dp.message_handler(commands=['exams', 'экзамены'])
async def exams_send(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Школьные экзамены"))
    poll_keyboard.add(types.KeyboardButton(text="ОГЭ"))
    poll_keyboard.add(types.KeyboardButton(text="ЕГЭ"))
    await message.answer("Экзамены", reply_markup=poll_keyboard)
    # await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    # await asyncio.sleep(0,5)
    # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Сессия-1.pdf', 'rb'))
    # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Сессия-2.pdf', 'rb'))
    # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//ЕГЭ ОГЭ.jpg', 'rb'))
    # await bot.send_message(message.from_user.id, (('Я скоро научусь отправлять расписание экзаменов💪')), parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    await bot.send_message(message.from_user.id, f"Здравствуйте, {message.from_user.first_name}!\nМеня зовут Электрон😎\n\
Я - бот Школы №1502\nЯ готов вам помочь😉\nДоступны следующие команды:\n/timetable - 🔔расписание уроков\
\n/statements - 📝заявления\n/hobby - 🎯кружки\n/consultations - 🤓расписание консультаций\n/calendar - 📅учеба и каникулы\
\n/exams - 📚расписание экзаменов\n/diagnostic - 👾ближайшие диагностические работы\n/ppv - 📝ППВ\n/inf \
- 🤔полезная информация\n/contacts - 🧑‍🚀контакты администрации школы и техподдержки\n/help - 🚑остались вопросы???\n/question - задать вопрос или оставить отзыв 🤗")
    inline_btn = InlineKeyboardMarkup()
    inline_btn_1 = InlineKeyboardButton('⚠️ИНСТРУКЦИЯ iphone⚠️', callback_data='btn1')
    inline_btn.add(inline_btn_1)
    inline_btn_2 = InlineKeyboardButton('⚠️ИНСТРУКЦИЯ android, windows⚠️', callback_data='btn2')
    inline_btn.add(inline_btn_2)
    inline_btn_3 = InlineKeyboardButton('🤔Задать вопрос🤔', callback_data='btn3')
    inline_btn.add(inline_btn_3)
    await message.answer("⚡Обязательно прочитайте инструкцию⚡", reply_markup=inline_btn)


@dp.message_handler(commands=['calendar', 'календарь'])
async def zayavleniya(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id,
                         photo=open('C://Users//admin//Desktop//Ggbot//Учебный календарь.png', 'rb'))


@dp.message_handler(commands=['ppv', 'ППВ'])
async def zayavleniya(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//ППВ.jpg', 'rb'))


# @dp.message_handler(commands=['voice'])
# async def process_voice_command(message: types.Message):
# await bot.send_voice(message.from_user.id, voice=open('C://Users//admin//Desktop//Ggbot//lalala.ogg', 'rb'))


# @dp.message_handler(commands=['note'])
# async def process_note_command(message: types.Message):
# user_id = message.from_user.id
# await bot.send_chat_action(user_id, ChatActionss.RECORD_VIDEO_NOTE)
# await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
# await bot.send_video_note(message.from_user.id, video_note=open('C://Users//admin//Desktop//Ggbot//video.mp4', 'rb'))


@dp.message_handler(commands=['inf'])
async def zayavleniya(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    keyboard = InlineKeyboardMarkup()
    url_button1 = InlineKeyboardButton(text="ГИА – 9, 11",
                                       url="http://obrnadzor.gov.ru/gosudarstvennye-uslugi-i-funkczii/7701537808-gosfunction/gosudarstvennaya-itogovaya-attestacziya-vypusknikov-11-klassov/")
    keyboard.add(url_button1)
    url_button2 = InlineKeyboardButton(text="Информация для ИТ- классов",
                                       url="http://profil.mos.ru/it/\nhttp://profil.mos.ru/it/?page_id=2193")
    keyboard.add(url_button2)
    url_button3 = InlineKeyboardButton(text="Информация для инженерных классов", url="http://profil.mos.ru/inj.html")
    keyboard.add(url_button3)
    url_button4 = InlineKeyboardButton(text="Информация для естественно-научных классов",
                                       url="http://profil.mos.ru/ntek.html")
    keyboard.add(url_button4)
    url_button5 = InlineKeyboardButton(text="Демо-варианты диагностических работ от МЦКО",
                                       url="https://mcko.ru/pages/m_n_d_i-m_materials")
    keyboard.add(url_button5)
    url_button6 = InlineKeyboardButton(text="Для желающих пройти независимую проверку знаний",
                                       url="https://mcko.ru/diagnostic_requests/new")
    keyboard.add(url_button6)
    url_button7 = InlineKeyboardButton(text="Субботы московского школьника", url="https://events.educom.ru/")
    keyboard.add(url_button7)
    await bot.send_message(message.chat.id, "ПОЛЕЗНАЯ ИНФОРМАЦИЯ", reply_markup=keyboard)


@dp.message_handler(commands=['diagnostic', 'диагностика'])
async def diagnostic_send(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(user_id, photo=open('C://Users//admin//Desktop//Ggbot//МЦКО1.png', 'rb'))
    await bot.send_photo(user_id, photo=open('C://Users//admin//Desktop//Ggbot//МЦКО2.png', 'rb'))


@dp.message_handler(commands=['contacts'])
async def contact_send(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    keyboard = InlineKeyboardMarkup()
    url_button8 = InlineKeyboardButton(text="САЙТ ШКОЛЫ", url="https://1502.mskobr.ru/#/")
    keyboard.add(url_button8)
    await bot.send_message(message.from_user.id, '8(495) 962-18-11 добавочный 805 — руководитель корпуса Бритов Денис Русланович;\n\
8(495) 963-19-11 добавочный 811 — методист корпуса Скалепова Лидия Васильевна;\n8(495) 963-08-59 добавочный 801 — секретарь корпуса Гамма;\n8(495) 963-47-78 добавочный 851 — социальные вопросы;\n8(495) 963-66-90 добавочный 804 — пост охраны;',
                           reply_markup=keyboard)


@dp.message_handler(commands=['hobby', 'кружки'])
async def hobby_send(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="7 класс"))
    poll_keyboard.add(types.KeyboardButton(text="8 класс"))
    poll_keyboard.add(types.KeyboardButton(text="9 класс"))
    poll_keyboard.add(types.KeyboardButton(text="10 класс"))
    poll_keyboard.add(types.KeyboardButton(text="11 класс"))
    await message.answer("КРУЖКИ", reply_markup=poll_keyboard)


@dp.message_handler(lambda message: message.text == "7 класс")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//7 класс.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "8 класс")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//8 класс.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "9 класс")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//9 класс.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "10 класс")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//10 класс.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "11 класс")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//11 класс.jpg', 'rb'))


@dp.message_handler(commands=['timetable', 'расписание'])
async def timetable_send(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="7Л"))
    poll_keyboard.add(types.KeyboardButton(text="7М"))
    poll_keyboard.add(types.KeyboardButton(text="7Н"))
    poll_keyboard.add(types.KeyboardButton(text="8Л"))
    poll_keyboard.add(types.KeyboardButton(text="8М"))
    poll_keyboard.add(types.KeyboardButton(text="8Н"))
    poll_keyboard.add(types.KeyboardButton(text="9Л"))
    poll_keyboard.add(types.KeyboardButton(text="9М"))
    poll_keyboard.add(types.KeyboardButton(text="9Н"))
    poll_keyboard.add(types.KeyboardButton(text="10Л"))
    poll_keyboard.add(types.KeyboardButton(text="10М"))
    poll_keyboard.add(types.KeyboardButton(text="10Н"))
    poll_keyboard.add(types.KeyboardButton(text="11Л"))
    poll_keyboard.add(types.KeyboardButton(text="11М"))
    await message.answer("РАСПИСАНИЕ", reply_markup=poll_keyboard)


@dp.message_handler(
    lambda message: message.text == "7л" or message.text == "7l" or message.text == "7 л" or message.text == "7 l" or message.text == "7 Л" or message.text == "7Л" or message.text == "7 L" or message.text == "7L")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//7л.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "7м" or message.text == "7m" or message.text == "7 м" or message.text == "7 m" or message.text == "7 М" or message.text == "7М" or message.text == "7 M" or message.text == "7M")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//7m.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "8л" or message.text == "8l" or message.text == "8 л" or message.text == "8 l" or message.text == "8 Л" or message.text == "8Л" or message.text == "8 L" or message.text == "8L")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open("C://Users//admin//Desktop//Ggbot//8l.png", 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "8м" or message.text == "8m" or message.text == "8 м" or message.text == "8 m" or message.text == "8 М" or message.text == "8М" or message.text == "8 M" or message.text == "8M")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//8m.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "8н" or message.text == "8n" or message.text == "8 н" or message.text == "8 n" or message.text == "8 Н" or message.text == "8Н" or message.text == "8 N" or message.text == "8N")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//8n.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "9л" or message.text == "9l" or message.text == "9 л" or message.text == "9 l" or message.text == "9 Л" or message.text == "9Л" or message.text == "9 L" or message.text == "9L")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//9l.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "9м" or message.text == "9m" or message.text == "9 м" or message.text == "9 m" or message.text == "9 М" or message.text == "9М" or message.text == "9 M" or message.text == "9M")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open("C://Users//admin//Desktop//Ggbot//9m.png", 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "9н" or message.text == "9n" or message.text == "9 н" or message.text == "9 n" or message.text == "9 Н" or message.text == "9Н" or message.text == "9 N" or message.text == "9N")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open("C://Users//admin//Desktop//Ggbot//9n.png", 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "10л" or message.text == "10l" or message.text == "10 л" or message.text == "10 l" or message.text == "10 Л" or message.text == "10Л" or message.text == "10 L" or message.text == "10L")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open("C://Users//admin//Desktop//Ggbot//10l.png", 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "10м" or message.text == "10m" or message.text == "10 м" or message.text == "10 m" or message.text == "10 М" or message.text == "10М" or message.text == "10 M" or message.text == "10M")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open("C://Users//admin//Desktop//Ggbot//10m.png", 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "10н" or message.text == "10n" or message.text == "10 н" or message.text == "10 n" or message.text == "10 Н" or message.text == "10Н" or message.text == "10 N" or message.text == "10N")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//10n.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "11я" or message.text == "11ya" or message.text == "11 я" or message.text == "11 ya" or message.text == "11 Я" or message.text == "11Я" or message.text == "11 YA" or message.text == "11YA")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//11ya.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "11л" or message.text == "11l" or message.text == "11 л" or message.text == "11 l" or message.text == "11 Л" or message.text == "11Л" or message.text == "11 L" or message.text == "11L")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//11l.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "11м" or message.text == "11m" or message.text == "11 м" or message.text == "11 m" or message.text == "11 М" or message.text == "11М" or message.text == "11 M" or message.text == "11M")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//11m.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(
    lambda message: message.text == "11н" or message.text == "11n" or message.text == "11 н" or message.text == "11 n" or message.text == "11 Н" or message.text == "11Н" or message.text == "11 N" or message.text == "11N")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//11n.png', 'rb'))
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Z9.png', 'rb'))


@dp.message_handler(commands=['statements', 'заявления'])
async def statements_send(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Об отсутствии контактов (Дошкольное образование)"))
    poll_keyboard.add(types.KeyboardButton(text="Об отсутствии контактов (Общее образование)"))
    poll_keyboard.add(types.KeyboardButton(text="Допуск к учебным занятиям"))
    poll_keyboard.add(types.KeyboardButton(text="Отсутствие на занятиях"))
    await message.answer("ЗАЯВЛЕНИЯ", reply_markup=poll_keyboard)


@dp.message_handler(commands=['консультации', 'consultations'])
async def consultations_send(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Русский язык"))
    poll_keyboard.add(types.KeyboardButton(text="Математика"))
    poll_keyboard.add(types.KeyboardButton(text="Физика"))
    poll_keyboard.add(types.KeyboardButton(text="Биология, химия, география, обществознание"))
    poll_keyboard.add(types.KeyboardButton(text="Английский язык"))
    poll_keyboard.add(types.KeyboardButton(text="Информатика"))
    await message.answer("КОНСУЛЬТАЦИИ", reply_markup=poll_keyboard)
    await bot.send_message(message.from_user.id, '❗❗❗❗❗❗\nКонсультации на каникулах 11.04-17.04👇')
    await bot.send_document(message.from_user.id, document=open('C://Users//admin//Desktop//Ggbot//7 класс.docx', 'rb'))
    await bot.send_document(message.from_user.id, document=open('C://Users//admin//Desktop//Ggbot//8 класс.docx', 'rb'))
    await bot.send_document(message.from_user.id, document=open('C://Users//admin//Desktop//Ggbot//9 класс.docx', 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open('C://Users//admin//Desktop//Ggbot//10  класс.docx', 'rb'))
    await bot.send_document(message.from_user.id,
                            document=open('C://Users//admin//Desktop//Ggbot//11 класс.docx', 'rb'))


@dp.message_handler(commands=['help'])
async def process_command_1(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    await bot.send_message(message.from_user.id, "Доступны следующие команды:\n/timetable - 🔔расписание уроков\
\n/statements - 📝заявления\n/hobby - 🎯кружки\n/consultations - 🤓расписание консультаций\n/calendar - 📅учеба и каникулы\
\n/exams - 📚расписание экзаменов\n/diagnostic - 👾ближайшие диагностические работы\n/ppv - 📝ППВ\n/inf \
- 🤔полезная информация\n/contacts - 🧑‍🚀контакты администрации школы и техподдержки\n/question - задать вопрос или оставить отзыв 🤗")
    inline_btn = InlineKeyboardMarkup()
    inline_btn_1 = InlineKeyboardButton('⚠️ИНСТРУКЦИЯ iphone⚠️', callback_data='btn1')
    inline_btn.add(inline_btn_1)
    inline_btn_2 = InlineKeyboardButton('⚠️ИНСТРУКЦИЯ android, windows⚠️', callback_data='btn2')
    inline_btn.add(inline_btn_2)
    inline_btn_3 = InlineKeyboardButton('🤔Задать вопрос🤔', callback_data='btn3')
    inline_btn.add(inline_btn_3)
    await message.answer("В какой категории вам потребуется помощь?", reply_markup=inline_btn)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               'Управлять ботом очень легко😊\nЧтобы получить нужную информацию, необходимо просто нажать на кнопку "Меню" или три полоски в левом нижнем углу экрана.')
        await asyncio.sleep(0, 5)
        await bot.send_message(callback_query.from_user.id, '❗❗❗❗❗❗')
        await bot.send_photo(callback_query.from_user.id,
                             photo=open('C://Users//admin//Desktop//Ggbot//instr2.png', 'rb'))
        await asyncio.sleep(0, 5)
        await bot.send_message(callback_query.from_user.id, '❗❗❗❗❗❗')
        await bot.send_message(callback_query.from_user.id, 'Для команд:\n/timetable\n/statements\n/hobby\n/consultations\n\
\nДоступна функция выбора категории👇')
        await asyncio.sleep(0, 5)
        await bot.send_photo(callback_query.from_user.id,
                             photo=open('C://Users//admin//Desktop//Ggbot//instr3.png', 'rb'))
    if code == 2:
        await bot.send_message(callback_query.from_user.id, '❗❗❗❗❗❗')
        await bot.send_message(callback_query.from_user.id,
                               'Чтобы выбрать команду, нужно написать "/" и сделать выбор из выпадающего списка:')
        await asyncio.sleep(0, 5)
        await bot.send_photo(callback_query.from_user.id,
                             photo=open('C://Users//admin//Desktop//Ggbot//Android.JPG', 'rb'))
        await bot.send_message(callback_query.from_user.id, '❗❗❗❗❗❗')
        await bot.send_message(callback_query.from_user.id, 'Для команд:\n/timetable\n/statements\n/hobby\n/consultations\n\
\nДоступна функция выбора категории👇')
        await asyncio.sleep(0, 5)
        await bot.send_photo(callback_query.from_user.id,
                             photo=open('C://Users//admin//Desktop//Ggbot//instr33.png', 'rb'))
    if code == 3:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, '👨‍💻Нажмите сюда, чтобы задать\nвопрос: /question')


@dp.message_handler(commands=['question'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Задайте свой вопрос:', reply_markup=cancel_keyboard)
    await Form.vopros.set()  # Устанавливаем состояние


# @dp.message_handler(commands=["help1502"])

# async def messages(message):
# 	if int(message.chat.id) == int(633675462):
# 		try:
# 			chatId=message.text.split(': ')[0]
# 			text=message.text.split(': ')[1]
# 			await bot.send_message(chatId, text)
# 		except:
# 			pass
# 	else:
# 		await bot.send_message(633675462, str(message.chat.id) + ': ' + message.text)
# 		await bot.send_message(message.chat.id, f'{message.from_user.first_name}, Ваш запрос принят. Мы уже получили его. Ожидайте 👍')


# @dp.callback_query_handler(lambda call: True)
# async def process_callback_button1(callback_query: types.CallbackQuery):
# if call.data == 'btn1':
# await bot.answer_callback_query(callback_query.id)
# await bot.send_photo(callback_query.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Снимок123.JPG', 'rb'))
# await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
# await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.message_handler(lambda message: message.text == "Русский язык")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Русский консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Математика")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Мат консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Физика")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Физика консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Биология, химия, география, обществознание")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id,
                         photo=open('C://Users//admin//Desktop//Ggbot//Биология консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Английский язык")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Англ консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Информатика")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Инф консул.png', 'rb'))


@dp.message_handler(lambda message: message.text == "Об отсутствии контактов (Дошкольное образование)")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id, document=open('C://Users//admin//Desktop//Ggbot//dou_notify.pdf', 'rb'))


@dp.message_handler(lambda message: message.text == "Об отсутствии контактов (Общее образование)")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id, document=open('C://Users//admin//Desktop//Ggbot//edu_notify.pdf', 'rb'))


@dp.message_handler(lambda message: message.text == "Школьные экзамены")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
    await asyncio.sleep(0, 5)
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Летняя сессия.png', 'rb'))
    await bot.send_message(message.from_user.id, "Расписание пробных экзаменов (ОГЭ/ЕГЭ)👇")
    await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//ЕГЭ ОГЭ.jpg', 'rb'))


@dp.message_handler(lambda message: message.text == "ОГЭ")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id, document=open('C://Users//admin//Desktop//Ggbot//ОГЭ.docx', 'rb'))


@dp.message_handler(lambda message: message.text == "ЕГЭ")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id, document=open('C://Users//admin//Desktop//Ggbot//ЕГЭ.docx', 'rb'))


@dp.message_handler(lambda message: message.text == "Допуск к учебным занятиям")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id, document=open('C://Users//admin//Desktop//Ggbot//after_absence.pdf', 'rb'))


@dp.message_handler(lambda message: message.text == "Отсутствие на занятиях")
async def action_cancel(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(0, 5)
    await bot.send_document(user_id,
                            document=open('C://Users//admin//Desktop//Ggbot//отсутствие на занятиях.pdf', 'rb'))


# @dp.message_handler()
# async def echo_message(msg: types.Message):
# await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(content_types=['text'])
async def xxx(message: types.Message):
    s = ''
    s1 = ''
    f = str(message.from_user.first_name)
    for i in range(len(f)):
        if f[i] != ' ' and f[i] not in A and f[i] not in B and f[i] not in C and f[i] not in D and f[i] not in E and f[i] not in Q:
            s += '?'
        elif f[i] == ' ':
            s += ' '
        else:
            s += f[i]
    g = str(message.from_user.last_name)
    for i in range(len(g)):
        if g[i] != ' ' and g[i] not in A and g[i] not in B and g[i] not in C and g[i] not in D and f[i] not in E and f[i] not in Q:
            s1 += '?'
        elif g[i] == ' ':
            s1 += ' '
        else:
            s1 += g[i]

    with open("C://Users//admin//Desktop//Ggbot//users.txt", "r") as JF:
        J = set()
        for line in JF:
            J.add(line.strip())
        if not (str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1) in J:
            JF = open("C://Users//admin//Desktop//Ggbot//users.txt", "a", encoding='ANSI')
            JF.write(str(message.chat.id) + ":" + str(message.from_user.username) + ":" + s + ":" + s1 + '\n')
            J.add(message.chat.id)
    if message.text == "PPV" or message.text == "ППВ" or message.text == "ппв" or message.text == "ppv":
        await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
        await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//ППВ.jpg', 'rb'))
    elif message.text == "Заявления" or message.text == "Заявление" or message.text == "заявление" or message.text == "заявления":
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Об отсутствии контактов (Дошкольное образование)"))
        poll_keyboard.add(types.KeyboardButton(text="Об отсутствии контактов (Общее образование)"))
        poll_keyboard.add(types.KeyboardButton(text="Допуск к учебным занятиям"))
        poll_keyboard.add(types.KeyboardButton(text="Отсутствие на занятиях"))
        await message.answer("ЗАЯВЛЕНИЯ", reply_markup=poll_keyboard)
    elif message.text == "Консультации" or message.text == "консультации" or message.text == "расписание консультаций" or message.text == "Расписание консультаций":
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Русский язык"))
        poll_keyboard.add(types.KeyboardButton(text="Математика"))
        poll_keyboard.add(types.KeyboardButton(text="Физика"))
        poll_keyboard.add(types.KeyboardButton(text="Биология, химия, география, обществознание"))
        poll_keyboard.add(types.KeyboardButton(text="Английский язык"))
        poll_keyboard.add(types.KeyboardButton(text="Информатика"))
        await message.answer("КОНСУЛЬТАЦИИ", reply_markup=poll_keyboard)
    elif message.text == "Ближайшие диагностические работы" or message.text == "ближайшие диагностические работы" or message.text == "Диагностические работы" or message.text == "диагностические работы" or message.text == "диагностика" or message.text == "Диагностика":
        await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
        await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//МЦКО1.jpg', 'rb'))
        await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//МЦКО2.jpg', 'rb'))
        await bot.send_document(message.from_user.id,
                                document=open('C://Users//admin//Desktop//Ggbot//Обязательные диагностики.docx', 'rb'))
    elif message.text == "Кружки" or message.text == "кружки":
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="7 класс"))
        poll_keyboard.add(types.KeyboardButton(text="8 класс"))
        poll_keyboard.add(types.KeyboardButton(text="9 класс"))
        poll_keyboard.add(types.KeyboardButton(text="10 класс"))
        poll_keyboard.add(types.KeyboardButton(text="11 класс"))
        await message.answer("КРУЖКИ", reply_markup=poll_keyboard)
    elif message.text == "Полезная информация" or message.text == "полезная информация":
        keyboard = InlineKeyboardMarkup()
        url_button1 = InlineKeyboardButton(text="ГИА – 9, 11",
                                           url="http://obrnadzor.gov.ru/gosudarstvennye-uslugi-i-funkczii/7701537808-gosfunction/gosudarstvennaya-itogovaya-attestacziya-vypusknikov-11-klassov/")
        keyboard.add(url_button1)
        url_button2 = InlineKeyboardButton(text="Информация для ИТ- классов",
                                           url="http://profil.mos.ru/it/\nhttp://profil.mos.ru/it/?page_id=2193")
        keyboard.add(url_button2)
        url_button3 = InlineKeyboardButton(text="Информация для инженерных классов",
                                           url="http://profil.mos.ru/inj.html")
        keyboard.add(url_button3)
        url_button4 = InlineKeyboardButton(text="Информация для естественно-научных классов",
                                           url="http://profil.mos.ru/ntek.html")
        keyboard.add(url_button4)
        url_button5 = InlineKeyboardButton(text="Демо-варианты диагностических работ от МЦКО",
                                           url="https://mcko.ru/pages/m_n_d_i-m_materials")
        keyboard.add(url_button5)
        url_button6 = InlineKeyboardButton(text="Для желающих пройти независимую проверку знаний",
                                           url="https://mcko.ru/diagnostic_requests/new")
        keyboard.add(url_button6)
        url_button7 = InlineKeyboardButton(text="Субботы московского школьника", url="https://events.educom.ru/")
        keyboard.add(url_button7)
        await bot.send_message(message.chat.id, "ПОЛЕЗНАЯ ИНФОРМАЦИЯ", reply_markup=keyboard)
    elif message.text == "Экзамены" or message.text == "экзамены" or message.text == "Расписание экзаменов" or message.text == "расписание экзаменов":
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Школьные экзамены"))
        poll_keyboard.add(types.KeyboardButton(text="ОГЭ"))
        poll_keyboard.add(types.KeyboardButton(text="ЕГЭ"))
        await message.answer("Экзамены", reply_markup=poll_keyboard)
        # await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
        # await asyncio.sleep(0,5)
        # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Сессия-1.pdf', 'rb'))
        # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//Сессия-2.pdf', 'rb'))
        # await bot.send_photo(message.from_user.id, photo=open('C://Users//admin//Desktop//Ggbot//ЕГЭ ОГЭ.jpg', 'rb'))
    elif message.text == "учебный календарь" or message.text == "Учебный календарь" or message.text == "каникулы" or message.text == "Каникулы" or message.text == "Календарь" or message.text == "календарь":
        await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_PHOTO)
        await bot.send_photo(message.from_user.id,
                             photo=open('C://Users//admin//Desktop//Ggbot//Учебный календарь.png', 'rb'))
    elif message.text == "Расписание" or message.text == "расписание" or message.text == "расписание уроков" or message.text == "Расписание уроков":
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="7Л"))
        poll_keyboard.add(types.KeyboardButton(text="7М"))
        poll_keyboard.add(types.KeyboardButton(text="8Л"))
        poll_keyboard.add(types.KeyboardButton(text="8М"))
        poll_keyboard.add(types.KeyboardButton(text="8Н"))
        poll_keyboard.add(types.KeyboardButton(text="9Л"))
        poll_keyboard.add(types.KeyboardButton(text="9М"))
        poll_keyboard.add(types.KeyboardButton(text="9Н"))
        poll_keyboard.add(types.KeyboardButton(text="10Л"))
        poll_keyboard.add(types.KeyboardButton(text="10М"))
        poll_keyboard.add(types.KeyboardButton(text="10Н"))
        poll_keyboard.add(types.KeyboardButton(text="11Л"))
        poll_keyboard.add(types.KeyboardButton(text="11Н"))
        poll_keyboard.add(types.KeyboardButton(text="11М"))
        poll_keyboard.add(types.KeyboardButton(text="11Я"))
        await message.answer("РАСПИСАНИЕ", reply_markup=poll_keyboard)
    elif message.text == "контакты" or message.text == "Контакты":
        keyboard = InlineKeyboardMarkup()
        url_button8 = InlineKeyboardButton(text="САЙТ ШКОЛЫ", url="https://1502.mskobr.ru/#/")
        keyboard.add(url_button8)
        await bot.send_message(message.from_user.id, '8(495) 962-18-11 добавочный 805 — руководитель корпуса Бритов Денис Русланович;\n\
8(495) 963-19-11 добавочный 811 — методист корпуса Скалепова Лидия Васильевна;\n8(495) 963-08-59 добавочный 801 — секретарь корпуса Гамма;\n8(495) 963-47-78 добавочный 851 — социальные вопросы;\n8(495) 963-66-90 добавочный 804 — пост охраны;',
                               reply_markup=keyboard)
    elif (message.text == "Статистика" or message.text == "статистика") and int(message.chat.id) == int(admin_chat_id):
        F = open('C://Users//admin//Desktop//Ggbot//users.txt', 'r')
        d = sum(1 for line in F) - 1
        if d != 12 and d < 100 and (str(d)[-1] == '2' or str(d)[-1] == '3' or str(d)[-1] == '4'):
            await bot.send_message(admin_chat_id, f'Cтатистика бота: *{d}* человекa', parse_mode=ParseMode.MARKDOWN)
            # await bot.send_document(admin_chat_id, document=open('C://Users//admin//Desktop//Ggbot//users.txt','rb'))
            # excel = 'C://Users//admin//Desktop//Ggbot//users.txt'
            # df = pd.read_csv(excel, sep=':',encoding='cp1251')
            # df.to_excel('C://Users//admin//Desktop//Ggbot//users.xlsx', index=False)
            # await bot.send_document(admin_chat_id, document=open('C://Users//admin//Desktop//Ggbot//users.xlsx', 'rb'))
            # path = os.path.join(os.path.abspath(os.path.dirname('C://Users//admin//Desktop//Ggbot//')), 'users.xlsx')
            # os.remove(path)
        else:
            await bot.send_message(admin_chat_id, f'Cтатистика бота: *{d}* человек', parse_mode=ParseMode.MARKDOWN)
            # await bot.send_document(admin_chat_id, document=open('C://Users//admin//Desktop//Ggbot//users.txt','rb'))
            # excel = 'C://Users//admin//Desktop//Ggbot//users.txt'
            # df = pd.read_csv(excel, sep=':',encoding='cp1251')
            # df.to_excel('C://Users//admin//Desktop//Ggbot//users.xlsx', index=False)
            # await bot.send_document(admin_chat_id, document=open('C://Users//admin//Desktop//Ggbot//users.xlsx', 'rb'))
            # path = os.path.join(os.path.abspath(os.path.dirname('C://Users//admin//Desktop//Ggbot//')), 'users.xlsx')
            # os.remove(path)
        excel = 'C://Users//admin//Desktop//Ggbot//users.txt'
        df = pd.read_csv(excel, sep=':', encoding='ANSI')
        df.to_excel('C://Users//admin//Desktop//Ggbot//users.xlsx', index=False)
        await bot.send_document(admin_chat_id, document=open('C://Users//admin//Desktop//Ggbot//users.xlsx', 'rb'))
        path = os.path.join(os.path.abspath(os.path.dirname('C://Users//admin//Desktop//Ggbot//')), 'users.xlsx')
        os.remove(path)

        F.close()
    elif int(message.chat.id) == int(admin_chat_id):
        chatId = message.text.split(': ')[0]
        text = bold('Вы спрашивали, мы отвечаем💪:') + '\n' + _join('Здравствуйте!') + '\n' + message.text.split(': ')[
            1] + '\n' + italic('С уважением техподдержка 👨‍💻')
        await bot.send_message(chatId, text, parse_mode=ParseMode.MARKDOWN)
    else:
        await bot.send_message(message.from_user.id,
                               "Я скоро научусь распознавать и это 💪\nA пока я тебя не понимаю🥺\nПроверь написание команды еще раз)\nВсегда готов помочь, просто нажми\n/help😊")


class Form(StatesGroup):
    vopros = State()  # Задаем состояние


@dp.message_handler(Text(equals="Отмена"), state="*")
async def menu_button(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(
        message.chat.id, "Обращение отменено.")

    await state.finish()


@dp.message_handler(state=Form.vopros)  # Принимаем состояние
async def start(message: types.Message, state: FSMContext):
    async with state.proxy() as proxy:  # Устанавливаем состояние ожидания
        proxy['vopros'] = message.text
    text = ''
    await bot.send_message(
        admin_chat_id,
        # f"Поступила заявка от @{message.from_user.username}\n\n"

        f"Поступило обращение от {message.chat.id}\n@{message.from_user.username}\n"
        f'Текст обращения: {proxy.get("vopros")}\n'
        ,

    )
    await bot.send_message(message.chat.id,
                           f'{message.from_user.first_name}, Ваше обращение отправлено. Мы уже получили его.\nОжидайте ответа😉')
    await state.finish()  # Выключаем состояние


if __name__ == '__main__':
    executor.start_polling(dp)