import discord
from discord.ext import commands
from discord import app_commands

class SteamReviewsNnApi(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
    

    @app_commands.command(name='predict', description="Predicts how you would rank some steam game based on your text.")
    async def preidct(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(f"If you're seeing this then the predict command works! Also, here is the text you've just entered: {text}")


async def setup(client: commands.Bot) -> None:  
        await client.add_cog(SteamReviewsNnApi(client))
    
    
        
    

