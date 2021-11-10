from aiogram import types
import unittest, bot, re

class MyTestCase(unittest.TestCase):
    async def test_echo(self):
        text_mock = "test123"
        message_mock = types.Message(text=text_mock)
        res = await bot.echo(message=message_mock)
        self.assertEqual(text_mock, res)

    async def test_flight(self):
        text_mock = "/show 3c6444"
        message_mock = types.Message(text=text_mock)
        res = await bot.show_handler(message=message_mock, regexp_command=re.match('show (\w{6})', text_mock))
        self.assertEqual(text_mock, res)

if __name__ == '__main__':
    unittest.main()
