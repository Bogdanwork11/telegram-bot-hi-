
import asyncio
from aiogram import Bot, Dispatcher,types
#aiogram всегда имеет асинхронность, и должен записан при помощи определенного синтаксиса
from aiogram.filters import CommandStart
#система фильтрации
bot = Bot(token='7726206191:AAHWmhuRm5jya8EpE7C7O4aNgcF3xKBKbgw')

dp = Dispatcher()#Обрабатывает обновления


#Обработчики(handler), декораторы(dpmessage)

@dp.message(CommandStart())
async def start_smd(message:types.Message)-> None:
    await message.answer('Приветсвую вас')

@dp.message()
async def echo(message:types.Message)-> None:
    text:str | None = message.text

    if text in ['Привет', 'привет', 'Здравствуйте', 'здравствуйте','Assalomu alaykum', 'assalomu alaykum', 'hi', 'Hi', 'Hello', 'hello']:
        await message.answer('Добро пожаловать!')
    elif text in ['Пока', 'пока', 'До свидания','до свидания' 'Bopti', 'bopti', 'bye', 'Bye']:
        await message.answer('До новых встреч! .....')
    else:
        await message.answer(message.text)




async def main()-> None: #Начало нашего бота
    await dp.start_polling(bot)

asyncio.run(main()) #Запуск нашего бота
