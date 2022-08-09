# controls blog management for aswinnnn.github.io
# created by Aswin S. | 24/07/2022


import subprocess
import discord
from discord.ext import commands
from pathlib import Path
from json import loads

config = []

def load_config():
    with open("config.json", "r") as f:
        conf = loads(f.read())
        config.append(conf)
    return

try:
    load_config()
    if config[0]["github-username"] == "the x in your x.github.io" or config[0]["discord-bot-token"] == "your discord bot token":
        print("\033[93m WARNING: Please take time to figure out your config.json\n Its in the README.md\033[0m")
        exit()

except:
    print("\033[93m WARNING: You Haven't set up the config.json correctly!!! \033[0m\n")
    exit()

config = config[0]

def create_blog(datetime: str, title: str, data: str) -> None:
    """
    ```
    create_blog("12 June 2023", "my testy tests", "so this is the most awesome test ever.")
    ```
    """
    base = Path(r"blog\base.html")
    with open(base, "r") as f:
        blog = f.read()
        blog = blog.replace("##DATETIME##", datetime)
        blog = blog.replace("##TITLE##", title)
        blog = blog.replace("##DATA##", data)
        
        try:
            with open(Path(rf"blog\{title}.html"), "x") as nf:
                nf.write(blog)
        except FileExistsError:
            with open(Path(rf"blog\{title}.html"), "r+") as nf:
                nf.write(blog)

def update_blog() -> None:
    subprocess.call("git add .")
    subprocess.call('git commit -am "new blog"')
    subprocess.call("git push origin main")   

def url(url: str) -> str:
    url = url.strip()
    url = url.split(" ")
    url = "%20".join(url)
    return url

def pretitle(tit: str) -> str:
    tit = tit.strip()
    tit = tit.split(" ")
    tit = " ".join(tit)
    return tit

TOKEN = config["discord-bot-token"]


# The only intent the bot needs (that has to be enabled) is "message content".
# This is just easy but if you do not wish to enable
# all intents of your discord bot, change the intents to only message content.
intents = discord.Intents.all() 


bot = commands.Bot(command_prefix=",", description="blog bot",intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")
    print("———————————")
    print("connected!")
    print("———————————")
    print("do ,help in chat to see all the commands")

blog = {}

@bot.command()
async def title(ctx, *,title: str):
    blog["title"] = pretitle(title)
    await ctx.send(f"{blog}")
 
@bot.command()
async def post(ctx):
    await ctx.send(f"{blog}")

@bot.command()
async def content(ctx, *,content: str):
    blog["content"] = content.replace("\n","<br>")
    await ctx.send(f"{blog}")

@bot.command()
async def clear(ctx):
    kills = []
    for k, v in blog.items():
        kills.append(k)

    for k in kills:
        blog.pop(k)
        
    await ctx.send("blog cleared.")

@bot.command()
async def date(ctx,*, date: str):
    blog["date"] = date
    await ctx.send(f"{blog}")

@bot.command()
async def upload(ctx):
    msg = await ctx.send("uploading...")
    create_blog(datetime=blog["date"], title=blog["title"], data=blog["content"])
    update_blog()
    await msg.edit(content=f'new blog added -> https://{config["your-github-username"]}.github.io/blog/{url(blog["title"])}.html')

bot.run(TOKEN)


    





