import discord
import json
import asyncio
import sqlite3
from discord.ext import commands


class NotifyCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def notify(self, ctx):
        # Ask for a Twitch Username
        await ctx.send("What is your Twitch Username?")

        def check(message):
            return message.author == ctx.author

        try:
            twitch_username_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
            twitch_username = twitch_username_msg.content.strip()

            # Ask for a Role ID to ping
            await ctx.send("Please enter the Role ID to ping:")

            try:
                # Wait for a message with the role ID
                role_id_msg = await self.bot.wait_for('message', check=check, timeout=60.0)
                notify_role_id = int(role_id_msg.content.strip())

                # Store the data in the SQLite database
                conn = sqlite3.connect('live-notify.db')
                cursor = conn.cursor()

                user_id = ctx.author.id

                # Insert data into the table
                cursor.execute('''
                    INSERT INTO twitch_users (user_id, twitch_username, notify_role_id)
                    VALUES (?, ?, ?)
                ''', (user_id, twitch_username, notify_role_id))

                # Commit the changes and close the connection
                conn.commit()
                conn.close()

                await ctx.send("Successfully added you to the notify list!")

            except ValueError:
                await ctx.send("Invalid Role ID. Please enter a valid Role ID.")
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond for the Role ID.")
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond for the Twitch Username.")

# TODO: Refactor code to allow the user to authorise their Twitch account and get the user ID from that following the
#  documentation found here: https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/

def setup(bot):
    bot.add_cog(NotifyCommand(bot))
