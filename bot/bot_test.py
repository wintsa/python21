import unittest, re
from aiogram import Bot, Dispatcher, types, filters
from config import BOT_TOKEN
from bot import echo, airplaneReply

"""
class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_echo(self):
        text_mock = "test123"
        message_mock = types.Message(text=text_mock)
        bot = Bot(token=BOT_TOKEN,
                       parse_mode=types.ParseMode.HTML,
                       )
        res = await echo(message=message_mock)
        self.assertEqual(text_mock, res)

    async def test_flight(self):
        text_mock = "/show 3c6444"
        message_mock = types.Message(text=text_mock)
        res = await bot.show_handler(message=message_mock, regexp_command=re.match('show (\w{6})', text_mock))
        self.assertEqual(text_mock, res)
"""

class ReplyTestCase(unittest.TestCase):
    def test_airplane(self):
        reply = airplaneReply('1f1d5d')
        self.assertRegex(reply, "Самолет находится в точке с коориднатами [0-9]*\.?[0-9]+, [0-9]*\.?[0-9]+ на высоте [0-9]*\.?[0-9]+ метров")

if __name__ == '__main__':
    unittest.main()
