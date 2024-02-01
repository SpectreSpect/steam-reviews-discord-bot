import discord
from discord.ext import commands
from discord import app_commands
from keras.preprocessing.text import Tokenizer
import pickle
import json
import requests


class SteamReviewsNnApi(commands.Cog):

    def get_tokenizer(self, pickle_file_path: str) -> Tokenizer:
        with open(pickle_file_path, 'rb') as handle:
            tokenizer = pickle.load(handle)
        return tokenizer


    def __init__(self, client: commands.Bot):
        self.client = client
        self.tokenizer = self.get_tokenizer("Tokenizer/tokenizer.pickle")


    def get_predictions(self, prompt: str):
        
        sequences = self.tokenizer.texts_to_sequences([prompt])
        data_to_send = json.dumps({'instances': sequences})
        model_url = f"http://localhost:8605/v1/models/AAAAAAAAAAAAAAAAAAAAAA:predict"
        predictions = requests.post(model_url, data=data_to_send)
        return predictions



    @app_commands.command(name='predict', description="Predicts how you would rank some steam game based on your text.")
    async def preidct(self, interaction: discord.Interaction, prompt: str):
        predictions = self.get_predictions(prompt)

        await interaction.response.send_message(f"Predictions: {predictions}")


async def setup(client: commands.Bot) -> None:  
    await client.add_cog(SteamReviewsNnApi(client))
    
