import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app
from config import OWNER_ID

@app.on_message(filters.command(['مهنتي'], prefixes=""))
def get_user_info(_, message):
    url = f"https://t.me/{message.from_user.username}"
    age = random.randint(15, 25)
    jobs = ["مدرس 👨‍🏫", "طبيب 👨‍⚕", "مهندس 👷‍♂", "خيال 🏇", "سباح 🏊", "مطور 👨‍💻"]
    job = random.choice(jobs)
    statuses = ["متزوج 👨‍👩‍👧‍👦", "اعذب 🧍‍♂", "مرتبط 👩‍❤️‍💋‍👨", "نرجسي 💆‍♂", "ملهم 🧝‍♂"]
    status = random.choice(statuses)
    inline_keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"↢ اسمك :  {message.from_user.first_name}", url=url)],
            [InlineKeyboardButton(f"↢ عمرك :  {age}", callback_data=f"age_{age}")],
            [InlineKeyboardButton(f"↢ مهنتك :  {job}", callback_data=f"job_{job}")],
            [InlineKeyboardButton(f"↢ حالتي :  {status}", callback_data=f"status_{status}")], 
            [InlineKeyboardButton("TepthonUserBot", url=f"https://t.me/tepthon")]
        ]
    )
    app.send_photo(
        chat_id=message.chat.id,
        photo=url,
        reply_markup=inline_keyboard
    )
