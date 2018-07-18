# L3NNY-Bot
L3NNY Bot is a discord selfbot ment to make your discord life easy. 

# Warning 
This is against Discord ToS and you using this puts your account at risk.

# How to set up
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/verixx/selfbot.py/tree/rewrite)


First go to heroku (press deploy to heroku) and then sign up or log in. Then after, [create a app](https://gyazo.com/0ca32142049cef8830aee7f73c50dcab) and name it whatever you want. Fork this respository and go to the [deploy tab](https://gyazo.com/f010fe70ba02e095da8d8d7476674506) on heroku. Next, link this respository to it. Next go on discord and do CTRL + ALT + I. Go to the application tab, and go all the way down until you see token. **Do not share this token.** Copy that token and go to the [settings tab](https://gyazo.com/6de113e39dc19980e9d3cd6528d1ac69) on heroku. Now, press [Reveal config vars](https://gyazo.com/3f237591c1a54bb1f1638fc72c9591d3) and paste in the token. Go back to deploy tab and press deploy. Now your done!

# Customize

Want to edit prefix? Go into the [bot.py](https://github.com/L3NNY0969/L3NNY-Bot/blob/master/bot.py) and find ```bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'), description="A bot made by L3NNY#0849\n\nHelp Commands", owner_id=411683912729755649)``` and edit the ```+``` to whatever prefix you want. 
**Tip:** Change it to something no one knows. Just to be safe.

Change ```owner_id=411683912729755649)``` in the bot.py and change it to your id.

This is being updated daily so make sure to check back often!
