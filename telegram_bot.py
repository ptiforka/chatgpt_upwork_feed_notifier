# telegram_bot.py

import asyncio
import logging
import telegram
from time import sleep
from telegram.ext import Updater, CommandHandler, MessageHandler
from rss_parser import get_latest_jobs_from_all_feeds
from chatgpt_sender import generate_custom_message_for_job

# Replace 'your_telegram_bot_token' with your Telegram bot token
TELEGRAM_BOT_TOKEN = 'telegram token'
CHANNEL_ID = 'channel id'
FEED_URLS_FILE = 'feed_urls.txt'

BOT = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_and_post_jobs():
    slept = 0
    job_entries = get_latest_jobs_from_all_feeds(FEED_URLS_FILE)
    print(job_entries)
    for job in job_entries:
        slept += 5
        custom_message = generate_custom_message_for_job(job)
        sleep(5)
        async with BOT:
            await BOT.send_message(chat_id=CHANNEL_ID, text=custom_message)
    return slept

# def setup_periodic_jobs(updater):
    # # Schedule the job to run every 5 minutes
    # job_queue = updater.job_queue
    # job_queue.run_repeating(fetch_and_post_jobs, interval=300, first=0)

async def main():
    minues_sleep = await fetch_and_post_jobs()
    sleep(300-minues_sleep)
#    time.sleep(300)
    # updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    # dp = updater.dispatcher

    # setup_periodic_jobs(updater)

    # updater.start_polling()
    # updater.idle()

while True:
    asyncio.run(main())
