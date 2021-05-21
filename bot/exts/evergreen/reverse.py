from contextlib import suppress
from typing import Optional

from discord import AllowedMentions, Embed, Forbidden
from discord.ext import commands

from bot.utils import helpers


class Reverse(commands.Cog):
    """Cog for the reverse command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["rev", "ᓚᘏᗢ"])
    async def reverse(self, ctx: commands.Context, *, text: Optional[str]) -> None:
        """
        Reverse the provided text
        If no text is given then the users nickname is reversed.
        """
        if not text:
            display_name = ctx.author.display_name

            display_name = display_name[::-1]

            await ctx.send(f"Your reversed nickname is: `{display_name}`", allowed_mentions=AllowedMentions.none())

            with suppress(Forbidden):
                await ctx.author.edit(nick=display_name)
        else:
            text = text[::-1]
            await ctx.send(
                f">>> {text}",
                allowed_mentions=AllowedMentions.none()
            )


def setup(bot: commands.Bot) -> None:
    """Loads the reverse cog."""
    bot.add_cog(Reverse(bot))