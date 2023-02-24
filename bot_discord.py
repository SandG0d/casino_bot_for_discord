import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send('chto-to')

bot.run("MTA3NDQwNjIyNTc3NDY1NzU2Nw.GeyWXX.Ch6rEajlceNJDhwVsdvynPrrq5ms7U8pSrZMdo")