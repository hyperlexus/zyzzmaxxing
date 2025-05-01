from discord.ext.commands import command, slash_command, Cog
from discord import Option
from datetime import date

import utils.data_manager


class GymCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="gym", description="Check in for your daily workout", guild_ids=[964302006091128893])
    async def gym(self, ctx):
        user_id = ctx.author.id
        user_data = utils.data_manager.get_user_data(self.bot.data, user_id)

        await ctx.respond("gym logged for today")
        today = str(date.today())
        if today in user_data["workouts"]:
            await ctx.respond("You have already logged today's workout")
            return

        user_data["workouts"].append(today)
        self.bot.save_data()
        await ctx.respond("Workout logged")
        print(self.bot.data)
        print(id, today)

    @slash_command(name="set_plan", description="Set your workout plan", guild_ids=[964302006091128893])
    async def set_plan(self, ctx, day: Option(str, "Add a day to your workout plan",
                        choices=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    ):
        await ctx.respond(f"{day} added to your plan")



def setup(bot):
    bot.add_cog(GymCog(bot))
