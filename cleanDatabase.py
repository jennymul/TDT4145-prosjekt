import os
from createDatabase import createDatabase
from fillDatabase import fillDatabase
import asyncio

if os.path.exists("trondelagTeater.db"):
    os.remove("trondelagTeater.db")


async def main():
    await createDatabase()
    await fillDatabase()


asyncio.run(main())
