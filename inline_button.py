from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
i = 1
keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="➖", callback_data="option1")
button2 = InlineKeyboardButton(text=f"{i}", callback_data="option2")
button3 = InlineKeyboardButton(text="➕", callback_data="option3")
keyboard.add(button1, button2, button3)