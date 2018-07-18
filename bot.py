import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'), description="A selfbot made by L3NNY#0849\n\nHelp Commands", owner_id=411683912729755649)


@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)


#@bot.command()
#async def uptime(ctx):
 #   """Get the bot's uptime"""
 #   color = discord.Color(value=0x00ff00)
 #   em = discord.Embed(color=color, title='Selfbot Uptime')
 #   em.description = f"{str(timedelta_str(datetime.datetime.now() - start_time)))"
 #   await ctx.send(embed=em)

    
@bot.command()
async def support(ctx):
    """Get help with the selfbot"""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Need help? Join!')
    em.description = f"https://discord.gg/FEPNu3A"
    await ctx.send(embed=em)
    
    
@bot.command()
async def info(ctx):
    """Get infomation about the selfbot"""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Infomation:')
    em.description = f"**Creator:** L3NNY#0849\n**Ping:**{bot.latency * 1000:.4f}\n**Servers you are in:** {len(bot.guilds)}"
    await ctx.send(embed=em)
                        

@bot.command(name='eval', hidden=True)
async def _eval(ctx, *, body):
    """Evaluates python code"""
    if not dev_check(ctx.author.id):
        return await ctx.send("You cannot use this because you are not a developer.")
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': bot._last_result,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text) - 1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:

                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')
    
    
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'), bot=False) 
