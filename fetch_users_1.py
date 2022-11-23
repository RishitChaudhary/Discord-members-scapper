from discord.ext import commands
import json

token='M..yODMzN.....OTQ5N..E3MA.GirWn7.nl08..HxOynI3lDFLT..u0pnZACS-pc'
guild_id = 446972765505847296

bot = commands.Bot(command_prefix="!", self_bot=True)
bot._skip_check = lambda x, y: False

@bot.event
async def on_ready():
    guild = bot.get_guild(guild_id)
    print(len(guild.members))
    member_count = guild.members[0].guild.member_count
    print(member_count)

    members_data_json = {}; members_fetched = 0
    for num in range(0,member_count):
        members_data_json[guild.members[num].id] = guild.members[num].name
        members_fetched += 1

    print(F"Members fetched: {members_fetched}")
    with open("users.json","w", encoding="utf-8") as f:
        json.dump(members_data_json, f)
    with open('ids.txt',"w") as file:
        for i in members_data_json:
            file.write(F"{i}\n")


bot.run(token, reconnect=True)

