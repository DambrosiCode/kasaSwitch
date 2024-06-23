import asyncio
from kasa import Discover

async def switch(ip, on):
  if on:
    dev = await Discover.discover_single(ip)
    await dev.turn_on()
    await dev.update()
  else:
    dev = await Discover.discover_single(ip)
    await dev.turn_off()
    await dev.update()