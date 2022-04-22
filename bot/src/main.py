import asyncio
import logging

import aioredis
from aiogram import Bot, Dispatcher, executor
from settings import API_TOKEN, CHANNEL_NAME, REDIS_JOBS_CHANNEL, REDIS_URL

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def redis_listener():
    redis = aioredis.from_url(REDIS_URL)
    subscription = redis.pubsub()
    await subscription.subscribe(REDIS_JOBS_CHANNEL)
    while True:
        message = await subscription.get_message(ignore_subscribe_messages=True)
        if message is not None:
            text = message["data"].decode("utf-8")
            await bot.send_message(CHANNEL_NAME, text)
            logging.info(f"Publishing {text}")
        await asyncio.sleep(5)


if __name__ == "__main__":
    executor.start(dp, redis_listener())
