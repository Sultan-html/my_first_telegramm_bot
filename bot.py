import asyncio
import logging
import random
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message
from aiogram.filters import command,CommandStart



bot = Bot(token='7424098226:AAHORON6F_NP7ewP0LvfXetxh2Qiexk8lQE')
dp = Dispatcher()

@dp.message(CommandStart())
async def start_bot(message: Message):
        await message.reply("""Привет, я тг бот по игре угадай число! Для того чтобы начать игру введите в чат: Я готов/я готова""")
        print("Для того чтобы начать игру введите в чат: Я готов/я готова")

@dp.message(F.text.in_({'Я готов', 'я готов', 'Я готова','я готова'}))
async def start_game(message: Message):
        await message.answer("Я загадал число от 1 до 3 угадайте его!")

@dp.message()
async def start_random(message: Message):
        user = int(message.text)
        number = random.choice([1, 2, 3])
        if user == number:
            await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
        else:
            await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")
        print(f"Загадонное число было {number}")
@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")