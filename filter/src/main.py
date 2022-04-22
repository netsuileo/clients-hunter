import asyncio
import logging

import aioredis
import async_timeout
from settings import (FILTERED_JOBS_CHANNEL, JOBS_SET, RAW_JOBS_CHANNEL,
                      REDIS_URL)

redis = aioredis.Redis.from_url(REDIS_URL, decode_responses=True)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


async def can_send_message(message):
    if await redis.sismember(JOBS_SET, message["data"]):
        return False
    await redis.sadd(JOBS_SET, message["data"])
    return True


async def filter_jobs():
    subscription = redis.pubsub()
    await subscription.subscribe(RAW_JOBS_CHANNEL)

    while True:
        try:
            async with async_timeout.timeout(1):
                message = await subscription.get_message(ignore_subscribe_messages=True)
                if message is None:
                    await asyncio.sleep(5)
                else:
                    if await can_send_message(message):
                        await redis.publish(FILTERED_JOBS_CHANNEL, message["data"])
                    else:
                        logging.info("Already sent this: %s", message["data"])
                    await asyncio.sleep(0.01)
        except asyncio.TimeoutError:
            pass


if __name__ == "__main__":
    asyncio.run(filter_jobs())
