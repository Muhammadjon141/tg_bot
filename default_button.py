from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Chevrolet"), KeyboardButton("BMW"), KeyboardButton("Mercedez Benz")],
    [KeyboardButton("Toyota"), KeyboardButton("Lixiang"), KeyboardButton("Leapmotor")],
    [KeyboardButton("UAZ")],
    [KeyboardButton("Jeep")]
        ],
    resize_keyboard=True)

menu_detail1 = ReplyKeyboardMarkup([
            [KeyboardButton("Damas"), KeyboardButton("Nexia")],
            [KeyboardButton("Cobalt"), KeyboardButton("Lacetti")],
            [KeyboardButton("Back")]],
            resize_keyboard=True)

menu_detail2 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail2.add(KeyboardButton("M5 Competation"), KeyboardButton("M8"))
menu_detail2.add(KeyboardButton("E 38"), KeyboardButton("M2"))
menu_detail2.add(KeyboardButton("Back"))

menu_detail3 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail3.add(KeyboardButton("S class"), KeyboardButton("E class"))
menu_detail3.add(KeyboardButton("G class"), KeyboardButton("W 223"))
menu_detail3.add(KeyboardButton("Back"))

menu_detail4 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail4.add(KeyboardButton("Camry"), KeyboardButton("Corrola"))
menu_detail4.add(KeyboardButton("Prado"), KeyboardButton("Land Cruiser"))
menu_detail4.add(KeyboardButton("Back"))

menu_detail5 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail5.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"))
menu_detail5.add(KeyboardButton("Mahsulot 3"), KeyboardButton("Mahsulot 4"))
menu_detail5.add(KeyboardButton("Back"))

menu_detail6 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_detail6.add(KeyboardButton("Mahsulot 1"), KeyboardButton("Mahsulot 2"))
menu_detail6.add(KeyboardButton("Mahsulot 3"), KeyboardButton("Mahsulot 4"))
menu_detail6.add(KeyboardButton("Back"))