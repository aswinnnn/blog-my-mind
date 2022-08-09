[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Top Language](https://img.shields.io/github/languages/top/aswinnnn/weheartpy)](https://img.shields.io/github/languages/top/aswinnnn/blog-my-mind) [![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
# blog-my-mind
Create blogs in Github Pages using Discord.

# How does it work?
- The `worker.py` is able to run a Discord bot which will have commands that you can use to update your blog in Github Pages.
- The program derives an html page from `base.html` and replaces placeholders for `date`, `title` and `content` to what you give it on discord.
- I originally came up with this to work on [my own blog](https://aswinnnn.github.io/) and it hasn't been bad. 
- The bot provides minimal functionality as it was made as a personal project. I will polish it depending on the attention it gets or you're more than welcome to open a PR.
  
# How to use
- clone this repo:
```
git clone https://github.com/aswinnnn/blog-my-mind.git
```
- The bot relies on `discord.py` (stable version) so make sure you got that.
- edit [config.json](config.json)
```
{"github-username": "the x in your x.github.io",
"discord-bot-token": "your discord bot token"}
```
- place the files in your `x.github.io` repo folder.
- run `python worker.py`
- requires Python `9` or above, tested on Python `10.4`.
  
# Using the bot
- Do `,help` in the discord chat after running `worker.py` and making sure the bot is in the server.
  
There are 4 basic commands:
- `date`: example: `,date 9 August 2022` or anything really, its a `str`.
- `title`: example: `,title My Perfect Blog`
- `content`: example: `,content This will be the content of your blog article. You are allowed to use html stylings in here such as <i> this </i> or <u> that </u>.`
- `post`: Lets you see the blog before uploading it.
- `upload`: Uploads the blog.

# Things to note:
- If you change the folder name from `blog` it will stop working until you change it in the code too.
- Don't forget to edit `base.html` and `index.html` according to your liking.
- the blog doesn't update `index.html`, you'll have to do it yourself.
- You can change the `base.html` but leave the placeholders alone, unless you update it in `worker.py`.

### Let me know about issues and you're always welcome to fork or pull request.