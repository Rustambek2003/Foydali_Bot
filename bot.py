from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

TOKEN = '5766174948:AAERI4lwWYzIfSPaLDBE9gWugxMpNAMgmVE'

def start(update: Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    keyboard = ReplyKeyboardMarkup([
        ['✳️ Tiktokdagi ilovalar'],
        ['🖥 Kompyuter uchun dasturlar', '📱 Smartfon uchun dasturlar'],
        ['📊 Statistika']
    ])

    bot.sendMessage(chat_id=chat_id,
    text = "𓅓 — bot sizning xizmatingizda! Siz asosiy menyudasiz!",
    reply_markup = keyboard
    )

def Statistika(update:Update, context:CallbackContext):
    chat_id = update.message.chat.id
    bot =context.bot
    bot.sendMessage(chat_id=chat_id,
    text="""👥 Botdagi obunachilar:  103099 ta

🔜 Oxirgi 24 soatda: 11 ta obunachi qo'shildi
🔝 Oxirgi 1 oyda: 509 ta obunachi qo'shildi
📆 Bot ishga tushganiga: 107 kun bo'ldi

📊  @Python_7760Bot statistikasi

Reklama uchun:👉 t.me/musulmon17"""
)

def Smarthone(update:Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    keyboard = ReplyKeyboardMarkup([
        ['Android', 'IOS'],
        ['🔙 Orqaga','🔝 Asosiy Menyu']
    ])
    bot.sendMessage(chat_id=chat_id,
    text = '𓅓 qaysi Smartfon tizimidan foydalanasiz?',
    reply_markup = keyboard
    )

def Android(update:Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    keyboar = ReplyKeyboardMarkup([
        ['Android dasturlar', "Android o'yinlar"],
        ['🔙 Orqaga','🔝 Asosiy Menyu']
    ])

    bot.sendMessage(chat_id=chat_id,
    text = "𓅓 sizga qaysi biri kerak? Dasturlar yoki o'yinlar?",
    reply_markup = keyboar
    )

def Android_d(update:Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Antivirus dasturlari',callback_data='anti'),InlineKeyboardButton(text='Office dasturlari',callback_data='office')],
        [InlineKeyboardButton(text='Video/Audio player',callback_data='video'),InlineKeyboardButton(text='Ijtimoiy tarmoqlar', callback_data='tarmoq')],
        [InlineKeyboardButton(text='VideoMontaj dasturlar',callback_data='montaj'),InlineKeyboardButton(text='Grafika dasturlari',callback_data='grafika')],
        [InlineKeyboardButton(text='VPN',callback_data='vpn'),InlineKeyboardButton(text='Fonga rasmlar',callback_data='fon')],
        [InlineKeyboardButton(text='Xarita',callback_data='xarita'),InlineKeyboardButton(text='Kamera',callback_data="kamera")],
        [InlineKeyboardButton(text='Torrent',callback_data='torrent'),InlineKeyboardButton(text='Sport',callback_data='sport')]
    ])
    bot.sendMessage(chat_id=chat_id,
    text = "Android dasturlari bo'limi, xohlagancha dasturlarni yuklab oling",
    reply_markup = keyboar
    )



def Kompyuter(update:Update, context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    keyboar = ReplyKeyboardMarkup([
        ['✳️  WINDOWS', '🍏 MAC OS'],
        ['🔙 Orqaga','🔝 Asosiy Menyu']
    ])

    bot.sendMessage(chat_id=chat_id,
    text = '𓅓 qaysi operatsion tizimdan foydalanasiz?',
    reply_markup = keyboar
    )


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🔝 Asosiy Menyu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📊 Statistika'),Statistika))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📱 Smartfon uchun dasturlar'),Smarthone))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🖥 Kompyuter uchun dasturlar'),Kompyuter))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Android'), Android))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Android dasturlar'),Android_d))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('IOS'),IOS))
updater.start_polling()
updater.idle()
