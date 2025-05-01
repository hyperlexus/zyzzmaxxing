from discord.ext.commands import command, slash_command, Cog
from discord import Option
from datetime import date

from utils.utils import last_included_weekday
import utils.data_manager

class GymCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="gym", description="Check in for your daily workout", guild_ids=[964302006091128893])
    async def gym(self, ctx):
        output_string = ""

        user_id = ctx.author.id
        user_data = utils.data_manager.get_user_data(self.bot.data, user_id)

        # check if streak is increased or broken
        last_included_day = last_included_weekday(user_data["plan"])
        print(last_included_day)

        today = str(date.today())
        if today in user_data["workouts"]:
            await ctx.respond("You have already logged today's gym")

        user_data["workouts"].append(today)
        user_data["last_workout"] = today
        self.bot.save_data()
        output_string += "gym logged for today"

        await ctx.respond(output_string)

    @slash_command(name="plan", description="Plan your workout", guild_ids=[964302006091128893])
    async def set_plan(self, ctx, day: Option(str, "Add a day to your workout plan",
                        choices=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]) = None
    ):
        user_id = ctx.author.id
        user_data = utils.data_manager.get_user_data(self.bot.data, user_id)

        print(user_data)

        if day is None:
            await ctx.respond(f"your workout plan is: {'no weekdays in your plan' if not user_data['plan'] else ', '.join(user_data['plan'])}")
            return

        if day in user_data["plan"]:
            user_data["plan"].remove(day)
            self.bot.save_data()
            await ctx.respond(f"{day} removed from your plan")
            return

        await ctx.respond(f"{day} added to your plan")
        user_data["plan"].append(day)
        self.bot.save_data()
        return




def setup(bot):
    bot.add_cog(GymCog(bot))
