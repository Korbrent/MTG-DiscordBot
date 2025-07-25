import os
import print
import interactions
from print import vprint
from config import BOT_TOKEN

# The holy Bot variable.
bot = interactions.Client(token = BOT_TOKEN)

"""
Load in the cog files from the ./cogs directory
"""
def load_cogs():
    # Iterate through the cog files
    for file in os.listdir('./cogs'):
        if file.endswith(".py") and not file.startswith('__'):
            cog = f'cogs.{file[:-3]}'
            try:
                bot.load(cog)
                vprint(print.DEBUG, f"Loaded extension: {cog}")
            except Exception as e:
                vprint(print.ERROR, f"Failed to load extension: {cog}\n{e}")


"""
On Ready event trigger to let us know that the bot has connected successfuly.
"""
@bot.event
async def on_ready():
    vprint(print.DEBUG, f"Logged in as {bot.me.name} (ID: {bot.me.id})")


"""
The Main function.
"""
def main():
    vprint(print.DEBUG, "Loading extensions...")
    load_cogs()
    vprint(print.DEBUG, "Extensions loaded. Starting bot...")
    bot.start()


if __name__ == "__main__":
    main()
