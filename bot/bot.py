import asyncio
import json
import urllib.request

from aiogram import Bot, Dispatcher, types, filters
from config import BOT_TOKEN

async def start_handler(event: types.Message):
    """
    Выдает приветствие
    """
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
    )

async def echo(message: types.Message):
    """
    Возвращает то, что получил
    """
    await message.answer(message.text)

async def main():
    """
    Основная функция работы с телеграмом
    """
    bot = Bot(token=BOT_TOKEN,
              parse_mode=types.ParseMode.HTML,
              )
    try:
        disp = Dispatcher(bot=bot)
        @disp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['show (\w{6})']))
        async def show_handler(message: types.Message, regexp_command):
            """
            Возвращает положение самолета по коду ICAO
            """
            path = "https://opensky-network.org/api/states/all?icao24="+regexp_command.group(1)
            data = urllib.request.urlopen(path).read()
            output = json.loads(data)
            states = output["states"]
            state = states[0]
            x = state[5]
            y = state[6]
            z = state[7]
            await message.reply(f"Самолет находится в точке с коориднатами {x}, {y} на высоте {z} метров")

        @disp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['show.*']))
        async def show_handler(message: types.Message, regexp_command):
            """
            Вспомогательная функция, если ввели некорректный код ИКАО
            """
            await message.reply(f"Введите /show и 6-значный код ИКАО")

        disp.register_message_handler(start_handler, commands={"start", "restart"})
        disp.register_message_handler(echo)
        await disp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())