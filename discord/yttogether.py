import discord
class ytTogether():
    url = "https://discord.gg/"
    async def ytTogether(self, voice_id):
        return self.url + (
            await self.bot.http.request(
                discord.http.Route(
                    "POST", f"/channels/{voice_id}/invites",
                ), json={
                    "max_age": 0,
                    "max_uses": 0,
                    "target_application_id": 755600276941176913,
                    "target_type": 2,
                    "temporary": False,
                    "validate": None
                }
                
            )
        )
