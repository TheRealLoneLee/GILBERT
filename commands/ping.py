import discord
from discord.ext import commands
import time
import datetime


class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = None  # Store the bot's start time (initially None)
        self.last_ping_time = None  # Store the last time the /ping command was run

    @commands.slash_command(
        name="ping",
        description="Shows the current status of the bot (Primarily for use by the Owner @TheRealLoneLee)"
    )
    async def ping(self, ctx):
        # Calculate uptime (time since the bot started)
        if self.start_time is None:
            self.start_time = time.time()  # Set the start time if it's not set
        end_time = time.time()
        uptime_seconds = round(end_time - self.start_time)
        uptime_formatted = self.format_time(uptime_seconds)

        # Calculate the response time of the bot
        if self.last_ping_time is not None:
            response_time_seconds = round((time.time() - self.last_ping_time), 2)
        else:
            response_time_seconds = None

        # Reset the last_ping_time
        self.last_ping_time = time.time()

        # Create an embed with the calculated values
        embed = discord.Embed(
            title="**__Here's a status update for you!__**",
            description=f"- Uptime: {uptime_formatted}\n",
            color=discord.Color.green()
        )

        if response_time_seconds is not None:
            emoji, color, image_path = self.get_response_time_info(response_time_seconds)
            embed.description += f"- {emoji} Response Time: {response_time_seconds} seconds\n"
            embed.color = color
            embed.set_image(url=image_path)  # Set the image as the main image of the embed

        embed.description += "\n**Key:**\n" \
                             "```" \
                             "- :green_circle: = I'm healthy and working like normal!\n" \
                             "- :orange_circle: = It's a bit of a slow day today.\n" \
                             "- :red_circle: = Please notify Lee IMMEDIATELY! I'M NOT OKAY OH GOD\n" \
                             "```"

        embed.set_footer(
            text="If you have any problems, please notify @TheRealLoneLee"
        )

        await ctx.send(embed=embed)

    def format_time(self, seconds):
        if seconds < 60:
            return f"{seconds} Seconds"
        elif seconds < 3600:
            minutes = seconds // 60
            seconds %= 60
            return f"{minutes} Minutes, {seconds} Seconds"
        else:
            hours = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            if minutes == 0:
                return f"{hours} Hours"
            return f"{hours} Hours, {minutes} Minutes"

    def get_response_time_info(self, response_time_seconds):
        if response_time_seconds < 50:
            return ":green_circle:", discord.Color.green(), "https://i.imgur.com/QTkBIMM.png"
        elif response_time_seconds < 125:
            return ":orange_circle:", discord.Color.orange(), "https://i.imgur.com/72sQl2u.png"
        else:
            return ":red_circle:", discord.Color.red(), "https://i.imgur.com/s0pHhdu.png"


def setup(bot):
    bot.add_cog(PingCommand(bot))
