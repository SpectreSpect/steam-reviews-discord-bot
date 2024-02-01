import os
from dotenv import load_dotenv
from discord import Intents, Client
from discord.ext import commands


class Client(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

        self.cogslist = ["cogs.SteamReviewsNnApi"]
    

    async def setup_hook(self):
        for ext in self.cogslist:
            await self.load_extension(ext)


    async def on_ready(self):
        await self.tree.sync()
        print(f"{self.user} is now running!")



if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    client = Client()
    client.run(token)