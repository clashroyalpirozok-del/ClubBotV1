import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Твой токен
BOT_TOKEN = "8902002895:AAHzNGjrwh3-dQndCFT1fp_-pgltn_fBc6c"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "👋 Привет!\n\n"
        "Открывай мини-апп и просматривай в реальном времени наши профеля\n\n"
        "Или подпишись на наш ТГК в нём мы иногда выкладываем новости"
    )
    
    builder = InlineKeyboardBuilder()
    
    # Кнопка с ссылкой на мини-приложение (откроется в браузере)
    builder.row(types.InlineKeyboardButton(
        text=" Открыть мини-апп",
        url="https://t.me/RozikOFFbot/Rozikoff/app"
    ))
    
    # Кнопка с подпиской на канал
    builder.row(types.InlineKeyboardButton(
        text="Подписаться на канал",
        url="https://t.me/ABSROZIK"
    ))
    
    await message.answer(text, reply_markup=builder.as_markup())

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
