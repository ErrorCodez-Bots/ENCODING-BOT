import os
import dns.resolver
from pyrogram import idle
from aiohttp import web
from . import app, log

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

async def hello(request):
    return web.Response(text="Bot is running successfully!")

async def main():
    server = web.Application()
    server.router.add_get("/", hello)
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    await app.start()
    await app.send_message(chat_id=log, text=f'<b>Bot Started! @{(await app.get_me()).username}</b>')
    await idle()
    await app.stop()

app.loop.run_until_complete(main())
