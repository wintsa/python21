import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ParseMode
from aiogram.utils import executor

from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types

bot = Bot(token=BOT_TOKEN,
          parse_mode=types.ParseMode.HTML, )
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# States
class Form(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    gender = State()  # Will be represented in storage as 'Form:gender'

@dp.message_handler(commands=['form']) #/form
async def start_request(event: types.Message):
    await Form.name.set()
    await event.reply("Hi there! What's your name?")

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user name
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("How old are you?")


# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def failed_process_age(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Form.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Male", "Female")
    markup.add("Other")

    await message.reply("What is your gender?", reply_markup=markup)

@dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Bad gender name. Choose your gender from the keyboard.")

@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Hi! Nice to meet you,', md.bold(data['name'])),
                md.text('Age:', md.code(data['age'])),
                md.text('Gender:', data['gender']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    # Finish conversation
    await state.finish()

@dp.message_handler(commands=['start', 'help']) #/start
async def start_handler(event: types.Message):
    print(event)
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!" + u"\U0001F1F7\U0001F1FA",
    )

@dp.message_handler(regexp='(^ships?$)') #ship or ships
async def ships(message: types.Message):
    print(message.text)
    with open('../img/ship.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Ship arrived')

@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['call (\+?[\d\-\(\)]*)'])) #/call 123
async def call(message: types.Message, regexp_command):
    print("call", regexp_command.group(1))
    await message.answer(f"Want to call <code>{regexp_command.group(1)}</code>")

@dp.message_handler()
async def echo(message: types.Message, state: FSMContext):
    print("echo", message.text)
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

"""
/start
/restart

"""
