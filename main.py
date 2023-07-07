#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Lx 0980

import asyncio
import logging
import uvloop
from pyromod import listen
from pyrogram import Client, enums
from config import Config

uvloop.install()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

DOWNLOAD_LOCATION = "./DOWNLOADS"

class ReplaceBot(Client):
    def __init__(self):
        super().__init__(
            session_name="ReplaceBot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            workers=20,
            plugins={'root': 'plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


if __name__ == "__main__":
    client = ReplaceBot()
    asyncio.run(client.start())
    client.run_until_disconnected()
