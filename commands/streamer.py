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
            twitch_username = await self.bot.wait_for('message', check=check, timeout=60.0)
            twitch_username = twitch_username.content.strip()
            
            # Ask for a Discord Channel ID
            await ctx.send("Please enter the Discord channel ID to notify people in:")
            
            try:
                # Wait for a message with the channel ID
                channel_id_message = await self.bot.wait_for('message', check=check, timeout=60.0)
                notify_channel_id = int(channel_id_message.content.strip())
                
                # Ask for a Role ID to ping
                await ctx.send("Please enter the Role ID to ping:")
                
                try:
                    # Wait for a message with the role ID
                    role_id_message = await self.bot.wait_for('message', check=check, timeout=60.0)
                    notify_role_id = int(role_id_message.content.strip())
                    
                    # Store the data in a database (e.g., SQLite or MySQL)
                    # Create a database schema (e.g., 'streamers' table)
                    # Example: store_data_in_database(ctx.author.id, twitch_username, notify_channel_id, notify_role_id)
                    
                    await ctx.send("Successfully added you to the notify list!")
                except ValueError:
                    await ctx.send("Invalid Role ID. Please enter a valid Role ID.")
                except TimeoutError:
                    await ctx.send("You took too long to respond for the Role ID.")
            except ValueError:
                await ctx.send("Invalid Channel ID. Please enter a valid Channel ID.")
            except TimeoutError:
                await ctx.send("You took too long to respond for the Channel ID.")
        except TimeoutError:
            await ctx.send("You took too long to respond for the Twitch Username.")
        
def setup(bot):
    bot.add_cog(NotifyCommand(bot))
