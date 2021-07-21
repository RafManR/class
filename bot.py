import asyncio
import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from config import token
from main import check_news_update


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("What's up?")


@dp.message_handler(commands="all_news")
async def get_all_news(message: types.Message):
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    for r, h in sorted(news_dict.items()):
       # news = f"<b>{datetime.datetime.fromtimestamp(h['article_date_timestamp'])}</b>\n" \
        #       f"<u>{h['article_title']}</u>\n" \
         #      f"<code>{h['article_desc']}</code>\n" \
          #     f"{h['article_url']}"
        #news = f"{hbold(datetime.datetime.fromtimestamp(h['article_date_timestamp']))}\n" \
               #f"{hunderline(h['article_title'])}\n" \
               #f"{hcode(h['article_desc'])}\n" \
               #f"{hlink(h['article_title'], h['article_url'])}"
        news = f"{hbold(datetime.datetime.fromtimestamp(h['article_date_timestamp']))}\n" \
               f"{hlink(h['article_title'], h['article_url'])}"


        await message.answer(news)
#    print(news_dict)

@dp.message_handler(commands="last_five")
async def get_last_five_news(message: types.Message):
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    for r, h in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(h['article_date_timestamp']))}\n" \
               f"{hlink(h['article_title'], h['article_url'])}"

        await message.answer(news)

@dp.message_handler(commands="fresh_news")
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for r, h in sorted(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(h['article_date_timestamp']))}\n" \
                   f"{hlink(h['article_title'], h['article_url'])}"

        await message.answer(news)

    else:
        await message.answer('No fresh news... ,SORRY')



if __name__ == '__main__':
    executor.start_polling(dp)