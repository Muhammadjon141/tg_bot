import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_detail1, menu_detail2, menu_detail3, menu_detail4, menu_detail5, menu_detail6
from inline_button import keyboard

API_TOKEN = "7232462327:AAFbEPknLYfZ_dYYGrSEeDJn0WluQ6U4Oq4"


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

commands = []

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    tg_id = message.from_user.id
    user_name = message.from_user.username
    full_data_new_user = [full_name, tg_id, user_name]
    Database.check_user_id(tg_id, full_data_new_user)
    query = f"INSERT INTO bot_users (full_name, user_name, tg_id) VALUES ('{user_name}', '{full_name}', {tg_id})"
    if await Database.check_user_id(tg_id, full_data_new_user):
        await message.reply(f"Assalomu aleykum sizni qayta ko'rganimdan xursandman  {full_name}", reply_markup=menu_keyboard)
    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {full_name}", reply_markup=menu_keyboard)
commands.append("/start")

@dp.message_handler(commands=["help"])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    await message.reply(f"Assalomu aleykum {full_name} muammoni yozib yuboring", reply_markup=menu_keyboard)

@dp.message_handler(lambda message: message.text == "Chevrolet")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Chevrolet mashinalarini tanlang:", reply_markup=menu_detail1)

commands.append("/help")

@dp.message_handler(lambda message: message.text == "BMW")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("BMW mashinalarini tanlang:", reply_markup=menu_detail2)

commands.append("BMW")

@dp.message_handler(lambda message: message.text == "Mercedez Benz")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Mercedez Benz mashinalarini tanlang:", reply_markup=menu_detail3)

commands.append("Mercedez Benz")

@dp.message_handler(lambda message: message.text == "Toyota")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Toyota mashinalarini tanlang:", reply_markup=menu_detail4)

commands.append("Toyota")

@dp.message_handler(lambda message: message.text == "Lixiang")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Lixiang mashinalarini tanlang:", reply_markup=menu_detail5)

commands.append("Lixiang")

@dp.message_handler(lambda message: message.text == "Leapmotor")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Leapmotor mashinalarini tanlang:", reply_markup=menu_detail6)

commands.append("Leapmotor")

@dp.message_handler(lambda message: message.text == "UAZ")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("UAZ mashinalarini tanlang ", reply_markup=menu_detail6)

@dp.message_handler(lambda message: message.text == "Jeep")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Jeep mashinalarini tanlang ", reply_markup=menu_detail6)

@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Toyota mashinalarini tanlang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Damas")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Damas sonini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "M5 Competation")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("M5 Competation sonini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "S class")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("S class sonini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Mahsulot 1 sonini tanlang:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Camry")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Camry sonini tanlang:", reply_markup=keyboard)

@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    if message.from_user.id in [6436571007]:
        await message.reply("Salom admin")
        photo_path = "telegram_bot/img.png"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
