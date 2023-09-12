import discord
from discord.ext import commands
import sqlite3

class NotifyChannelCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def notifychannel(self, ctx):
        # Check if the user has the appropriate permissions (e.g., admin)
        if ctx.author.guild_permissions.administrator:
            await ctx.send("Please provide the ID of the channel where you want notifications to be sent.")

            def check(message):
                return message.author == ctx.author

            try:
                channel_id_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
                channel_id = channel_id_msg.content.strip()

                # Check if the provided ID is a valid channel ID
                try:
                    channel = self.bot.get_channel(int(channel_id))
                    if not channel:
                        raise ValueError
                except ValueError:
                    await ctx.send("Invalid channel ID. Please provide a valid channel ID.")
                    return

                # Update the global notification channel ID in the config table
                conn = sqlite3.connect('live-notify.db')
                cursor = conn.cursor()

                cursor.execute('INSERT OR REPLACE INTO config (notify_channel_id) VALUES (?)', (channel.id,))
                conn.commit()
                conn.close()

                await ctx.send(f"Notifications will now be sent to {channel.mention}.")

            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond.")
        else:
            await ctx.send("You don't have the required permissions to set the notification channel.")

def setup(bot):
    bot.add_cog(NotifyChannelCommand(bot))
