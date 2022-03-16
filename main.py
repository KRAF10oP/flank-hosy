import os
os.system("pip install discord_buttons_plugin")
os.system("pip install discord-py-slash-command")
os.system("pip install enhanced-dpy")
import colorama
import discord
import asyncio
import requests
from time import strftime
from webserver import keep_alive
from discord.utils import find
from discord.ext import commands, tasks
from discord_buttons_plugin import *
import time
import datetime
from discord.ext.commands import Greedy
from typing import Union
from discord_slash import SlashCommand, SlashContext

token = os.environ['token']

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.Bot(command_prefix=commands.when_mentioned_or("$"), case_insensitive=True, intents=intents , help_command= None)
slash = SlashCommand(client, sync_commands=True)
buttons = ButtonsClient(client)
headers={"Authorization": f'{token}'}



@client.event
async def on_connect():
  print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m] Connected To [\x1b[38;5;213m{client.user}\x1b[38;5;15m]')
  watch = discord.Activity(type = discord.ActivityType.watching, name=f'$help & /help')
  await client.change_presence(status=discord.Status.idle, activity=watch)

@client.event
async def on_guild_remove(guild):
  log_channel = client.get_channel(928254198821310475)
  embed = discord.Embed(title='Flank Security', color=0x2f3136, description=f'Removed From A Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png')
  await log_channel.send(embed=embed)



@client.group(invoke_without_command = True)
async def security(ctx):
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection" , description="<a:bttt_load:953311223456354394> **Anti Ban**\n<a:bttt_load:953311223456354394> **Anti Kick**\n<a:bttt_load:953311223456354394> **Anti Unban**\n<a:bttt_load:953311223456354394> **Anti Bot Add**\n<a:bttt_load:953311223456354394> **Anti Channel Create**\n<a:bttt_load:953311223456354394> **Anti Channel Delete**\n<a:bttt_load:953311223456354394> **Anti Channel Update**\n<a:bttt_load:953311223456354394> **Anti Role Create**\n<a:bttt_load:953311223456354394> **Anti Role Delete**\n<a:bttt_load:953311223456354394> **Anti Role Update**\n<a:bttt_load:953311223456354394> **Anti Prune**\n<a:bttt_load:953311223456354394> **Anti Webhookspam**\n<a:bttt_load:953311223456354394> **Anti Guild Update**\n<a:bttt_load:953311223456354394> **Anti Emoji Delete**\n<a:bttt_load:953311223456354394> **Anti Emoji Create**\n<a:bttt_load:953311223456354394> **Anti Emoji Update**\n<a:bttt_load:953311223456354394> **Anti Role Update**\n<a:bttt_load:953311223456354394> **Anti Everyone Ping**\n<a:bttt_load:953311223456354394> **Anti Selfbot**\n`Credits to Sky for helping with Anti Nuke`")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.reply(embed = embed , mention_author = False)

@client.group()
async def moderation(ctx):
    embed = discord.Embed(color = 0x2f3136)
    embed.set_author(name = "Flank Protection Moderation Commands")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.add_field(name = "<:bt_announcements:944623279208022086> Mute" , value = "```Mute's a member```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Unmute" , value = "```Unmute's a member```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Lock" , value = "```Lock's a channel```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Unlock" , value = "```Unlock's a channel```" , inline = False)
    await ctx.reply(embed = embed , mention_author = False)

@client.event
async def on_guild_join(guild):
  log_channel = client.get_channel(928254198821310475)
  channel = guild.text_channels[0]
  invlink = await channel.create_invite(unique = True)
  embed = discord.Embed(title='Flank Protection', color=0x2f3136, description=f'Joined New Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953163625915367454/protection-1.png')
  embed.add_field(name = "Link Of Server" , value = f'{invlink}')
  await log_channel.send(embed=embed)

@client.event
async def on_member_join(member):
    guild = member.guild
    reason = "Flank Protection | Anti-Bot-Add"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
    logs = logs[0]
    if member.bot:
      await member.ban(reason=f"{reason}")
      await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_kick(member):
    guild = member.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
    logs = logs[0]
    reason = "Flank Protection| Kicking Members"
    await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_remove(member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "Flank Protection| Anti Prune"
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_ban(guild, member : discord.Member):
    reason = "Flank Protection | Anti-Ban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")
    await guild.unban(user=member, reason="Anti Ban")


@client.event
async def on_member_unban(guild, member : discord.Member):
    reason = "Flank Protection | Anti-Unban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_channel_delete(channel):
  reason = "Flank Protection | Anti Channel Delete"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  if isinstance(channel, discord.TextChannel):
      await guild.create_text_channel(channel.name, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
  if isinstance(channel, discord.VoiceChannel):
      await guild.create_voice_channel(f"{channel}")


@client.event
async def on_guild_update(before, after):
  reason = "Flank Protection | Guild Update"
 # guild = after.guild
  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  await after.edit(name=f"{before.name}")

@client.event
async def on_member_update(before, after):
  reason = "Flank Protection | Member Update"
  logs = await before.guild.audit_logs(limit=1,action=discord.AuditLogAction.member_role_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason = f"{reason}")
  
@client.event
async def on_guild_channel_create(ch):
    try:
        async for entry in ch.guild.audit_logs(limit = 1 , action = discord.AuditLogAction.channel_create):
            await ch.guild.ban(entry.user , reason = "Flank Protection | Anti Channel")
            await ch.delete()
    except Exception as e:
        print(e)

@client.event
async def on_message(message):
  await client.process_commands(message)
  member = message.author
  guild = message.guild
  if message.mention_everyone:
    if member == guild.owner:
      pass
    else:
      await message.delete()
      await member.kick(reason="Flank Protection | Mentioning everyone/here")
  else:
    if message.embeds:
      if member.bot:
        pass
      else:
        await member.kick(reason="Flank Protection | Anti Selfbot")

@client.event
async def on_guild_role_create(role):
  reason = "Flank Protection | Anti Role Create"
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  await role.delete()


@client.event
async def on_guild_role_delete(role):
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
  reason = "Flank Protection | Anti Role Delete"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  await guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_create).flatten()
  reason = "Flank Protection | Anti Emoji Create"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")
  await guild.emoji_delete()

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_delete).flatten()
  reason = "Flank Protection | Anti Emoji Delete"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_update).flatten()
  reason = "Flank Protection | Anti Emoji Update"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")


@client.event
async def on_guild_role_update(before, after):
  reason = "Flank Protection | Anti Role Update"
  guild = after.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_channel_update(before, after):
  reason = "Flank Protection | Anti Channel Update"
  guild = after.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_webhook_update(webhook):
  reason = "Flank Protection | Anti Webhook"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")


@client.event
async def on_webhooks_update(webhook):
  reason = "Flank Protection | Anti Webhook"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}") 


@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Information', color=0x2f3136)
    embed.add_field(name='Name', value='```Flank Protection```', inline=False)
    embed.add_field(name='Server Count', value=f'```{len(client.guilds)}```', inline=False)
    embed.add_field(name='User Count', value=f'```{len(set(client.get_all_members()))}```', inline=False)
    embed.add_field(name='Ping', value=f'```{int(client.latency * 1000)}```', inline=False)
    embed.add_field(name='Discord.py', value=f'```1.7.3```', inline=False)
    embed.add_field(name='Creators', value=f'```Sky & Jack & Ghost & Toxic```', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png')
    await ctx.reply(embed=embed)

@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    embed=discord.Embed(color=0x2f3136, title = '**Flank Protection**' , timestamp=ctx.message.created_at, description=f'```{error}```')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection", icon_url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    await ctx.reply(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=15):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def serverinfo(ctx):
  guild_roles = len(ctx.guild.roles)
  guild_categories = len(ctx.guild.categories)
  guild_members = len(ctx.guild.members)
  text_channels = len(ctx.guild.text_channels)
  voice_channels = len(ctx.guild.voice_channels)
  channels = text_channels + voice_channels
  serverinfo = discord.Embed(colour=0x2f3136)
  serverinfo.add_field(name="Server Name", value=f"```{ctx.guild.name}```" , inline = False)
  serverinfo.add_field(name="Server ID", value=f"```{ctx.guild.id}```", inline = False)
  serverinfo.add_field(name="Server Owner", value=f"```{ctx.guild.owner}```", inline = False)
  serverinfo.add_field(name="Boosts", value=f"```{ctx.guild.premium_subscription_count}```", inline = False)
  serverinfo.add_field(name="Channels", value=f"```{channels}```", inline = False)
  serverinfo.add_field(name="Roles", value=f"```{guild_roles}```", inline = False)
  serverinfo.add_field(name="Categories", value=f"```{guild_categories} Categories```", inline = False)
  serverinfo.add_field(name="Members", value=f"```{guild_members}```", inline = False)
  serverinfo.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=serverinfo)


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    if member == '':
        member = ctx.author
    format = "%d-%m-%Y"
    member = ctx.author if not member else member
    member_roles = len(member.roles)
    serverinfo = discord.Embed(colour=0x2f3136)
    serverinfo.add_field(name="Username", value=f"```{member}```" , inline= False)
    serverinfo.add_field(name="User ID", value=f"```{member.id}```", inline= False)
    serverinfo.add_field(name="Created At", value=f"```{member.created_at.strftime(format)}```", inline= False)
    serverinfo.add_field(name="Joined At", value=f"```{member.joined_at.strftime(format)}```", inline= False)
    serverinfo.add_field(name="Roles", value=f"```{member_roles}```", inline= False)
    serverinfo.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=serverinfo)

@client.command()
async def invite(ctx):
	embed = discord.Embed(title=f"Invite {client.user.name}", color=0x2f3136, description=f"[Click Here To Invite](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands)")
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands"
				)
			])
		]
	) 

@client.group(invoke_without_command = True)
async def utility(ctx):
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection")
        #embed.set_thumbnail(url="https://i.imgur.com/ZUbZ55y.gif")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection")
    embed.add_field(name="<:bt_announcements:944623279208022086> Purge", value="```Clear all messages```" , inline = False)   
    embed.add_field(name="<:bt_announcements:944623279208022086> Banner", value="```Show's userbanner```" , inline = False)
    embed.add_field(name="<:bt_announcements:944623279208022086> Serverinfo", value="```Show's Serverinfo```" , inline = False)
    embed.add_field(name="<:bt_announcements:944623279208022086>> Userinfo", value="```Show's info of a user```" , inline = False)
    embed.add_field(name="<:bt_announcements:944623279208022086> Membercount", value="```Show's member's in a server```" , inline = False)
    await ctx.reply(embed = embed , mention_author = False)


@client.group()
async def help(ctx):
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name="Flank Protection")
    embed.set_thumbnail (url="https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Security" ,  icon_url= "https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.add_field(name="<a:bttt_settings_2:953315884217303060> Help", value="```Show's Help command```" , inline = False)
    embed.add_field(name="<:bttt_Mod:953318240715685948> Moderation", value="```Show's  Moderation command```" , inline = False)
    embed.add_field(name="<a:bt_musicc:938791114654220310> Utility", value="```Show's Utility command```" , inline = False)
    embed.add_field(name="<a:bttt_securitysafe:953316089775931482> Security", value="```Show's Security command```" , inline = False)
    embed.add_field(name = "<:bt_Security:952869522178723860> Botinfo" , value =  "```Show's info about the bot```")
    await ctx.reply(embed = embed , mention_author = False)

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection |Locked Channel")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/928254198821310475/953502323357929522/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection")
    embed.add_field(name="<a:bt_tick:938659264258514944> Locked", value="```Channel has been locked```" , inline = False)
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://cdn.discordapp.com/attachments/941566343189237801/953261356046487562/a833aced3a3684a0bd3dc0200ae4a482.png")
    await ctx.reply(embed = embed , mention_author = False)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection |Unlocked Channel")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection")
    embed.add_field(name="<a:bt_tick:938659264258514944> Unlocked", value="```Channel has been unlocked```",inline = False)
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    await ctx.reply(embed = embed , mention_author = False)




  

@client.command(aliases=["mc"])
async def membercount(ctx):
    embed = discord.Embed(title='Flank Protection Anti Nuke', color=0x2f3136)
    embed.add_field(name="Server Members :", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
    embed.set_footer(text="Flank Protection Security", icon_url=
              "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    await ctx.reply(embed=embed)


@client.command()
async def banner(ctx, user:discord.Member):
    if user == None:
       user = ctx.author
    bid = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]
    
    if banner_id:
       embed = discord.Embed(color= 0x2f3136)
       embed.set_author(name=f"{user.name}'s Banner")
       embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
       await ctx.reply(embed = embed)
    else:
       embed = discord.Embed(title='Flank Protection Security', color=0x2f3136, description=f"**`User has no banner`**")
       await ctx.reply(embed = embed)

@client.command(aliases=["av"])
async def pfp(ctx, member : discord.Member = None):
    member = ctx.author if not member else member

    lund = discord.Embed(
    title = f"**{member.name}'s Profile Picture**",
    color = 0x2f3136
    )
    lund.set_image(url='{}'.format(member.avatar_url))
    await ctx.reply(embed=lund)

@client.command()
@commands.has_permissions(manage_emojis = True)
async def steal(ctx, emotes: Greedy[Union[discord.Emoji, discord.PartialEmoji]]):
    if not emotes:
        return await ctx.send('You didn\'t specify any emotes >:(')
    in_server, added = [], []
    for emote in emotes:
        if isinstance(emote, discord.Emoji) and emote.guild == ctx.guild:
            in_server.append(emote)
        else:
            added.append(await ctx.guild.create_custom_emoji(
                name=emote.name,
                image=await emote.url.read(),
                reason=f'Added by {ctx.author} ({ctx.author.id})'))

    if not added:
        return await ctx.send(f'Specified emote{"s" if len(emotes) != 1 else ""} are already in this server >:(')
    if in_server:
        return await ctx.send(f'{" ".join(map(str, added))} have been added to this server, while '
                              f'{" ".join(map(str, in_server))} wasn\'t because they are already added!')
    await ctx.send(f'{" ".join(map(str, added))} has been added to this server!')

@client.command()
async def enlarge(ctx , emoji: discord.PartialEmoji = None):
  embed = discord.Embed(title = f"Emoji Name | {emoji.name}" , color = 0x2f3136)
  embed.set_image(url=  f'{emoji.url}')
  embed.set_author(name=f"Requested by{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
  await ctx.reply(embed = embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False)#, read_message_history=True, read_messages=False , view_channels = True
                
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(color=0x2097FD , title="Flank Protection")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.add_field(name="<a:bt_tick:938659264258514944> Muted", value=f"```Muted- ```{member.mention}" , inline = False)
    embed.set_footer(text="Flank Protection", icon_url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")

    await ctx.reply(embed = embed , mention_author = False)

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(color=0x2097FD , title="Flank Protection")
    embed.add_field(name="<a:bt_tick:938659264258514944> Muted", value=f"```Unmuted-```{member.mention}" , inline = False)
    embed.set_footer(text="Flank Protection", icon_url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    await ctx.reply(embed = embed , mention_author = False)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="Flank Protection", description=f"**<a:bt_tick:938659264258514944> Latency is `{int(client.latency * 1000)}` ms**", colour=0x2f3136) 
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
  embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
  await ctx.reply(embed=embed)

#slash commands

@slash.slash(description="shows help page")
async def help(ctx: SlashContext):
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name="Flank Protection")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.add_field(name="<a:bttt_load:953311223456354394> Help", value="```Show's Help command```" , inline = False)
    embed.add_field(name="<a:bttt_load:953311223456354394> Moderation", value="```Show's  Moderation command```" , inline = False)
    embed.add_field(name="<a:bttt_load:953311223456354394> Utility", value="```Show's Utility command```" , inline = False)
    embed.add_field(name="<a:bttt_load:953311223456354394> Security", value="```Show's Security command```" , inline = False)
    embed.add_field(name = "<a:bttt_load:953311223456354394> Botinfo" , value =  "```Show's info about the bot```")
    await ctx.reply(embed = embed)

@slash.slash(description="shows bot latency")
async def ping(ctx: SlashContext):
  embed = discord.Embed(title="Flank Protection", description=f"<a:load:914814708232618044> **Latency is `{int(client.latency * 1000)}` ms**", colour=0x2f3136) 
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
  embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
  await ctx.reply(embed=embed)

@slash.slash(description="shows security page")
async def security(ctx: SlashContext):
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection" , description="<a:bttt_load:953311223456354394> **Anti Ban**\n<a:bttt_load:953311223456354394> **Anti Kick**\n<a:bttt_load:953311223456354394> **Anti Unban**\n<a:bttt_load:953311223456354394> **Anti Bot Add**\n<a:bttt_load:953311223456354394> **Anti Channel Create**\n<a:bttt_load:953311223456354394> **Anti Channel Delete**\n<a:bttt_load:953311223456354394> **Anti Channel Update**\n<a:bttt_load:953311223456354394> **Anti Role Create**\n<a:bttt_load:953311223456354394> **Anti Role Delete**\n<a:bttt_load:953311223456354394> **Anti Role Update**\n<a:bttt_load:953311223456354394> **Anti Prune**\n<a:bttt_load:953311223456354394> **Anti Webhookspam**\n<a:bttt_load:953311223456354394> **Anti Guild Update**\n<a:bttt_load:953311223456354394> **Anti Emoji Delete**\n<a:bttt_load:953311223456354394> **Anti Emoji Create**\n<a:bttt_load:953311223456354394> **Anti Emoji Update**\n<a:bttt_load:953311223456354394> **Anti Role Update**\n<a:bttt_load:953311223456354394> **Anti Everyone Ping**\n<a:bttt_load:953311223456354394> **Anti Selfbot**\n`Credits to Sky for helping with Anti Nuke`")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.reply(embed = embed)

@slash.slash(description="shows moderation commands")
async def moderation(ctx: SlashContext):
    embed = discord.Embed(color = 0x2f3136)
    embed.set_author(name = "Flank Protection Moderation Commands")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection" ,  icon_url= "https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png") 
    embed.add_field(name = "<:bt_announcements:944623279208022086> Mute" , value = "```Mute's a member```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Unmute" , value = "```Unmute's a member```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Lock" , value = "```Lock's a channel```" , inline = False)    
    embed.add_field(name = "<:bt_announcements:944623279208022086> Unlock" , value = "```Unlock's a channel```" , inline = False) 
    await ctx.reply(embed = embed)


@slash.slash(description="shows utility commands")
async def utility(ctx: SlashContext):
    embed = discord.Embed(color=0x2f3136 , title="Flank Protection")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png")
    embed.set_footer(text="Flank Protection")
    embed.add_field(name="<:900611921928126484:906858683508600852> Avatar", value="```Show's avatar of a user```" , inline = False)   
    embed.add_field(name="<:900611921928126484:906858683508600852> Banner", value="```Show's userbanner```" , inline = False)   
    embed.add_field(name="<:900611921928126484:906858683508600852> Serverinfo", value="```Show's Serverinfo```" , inline = False)
    embed.add_field(name="<:900611921928126484:906858683508600852> Userinfo", value="```Show's info of a user```" , inline = False)
    embed.add_field(name="<:900611921928126484:906858683508600852> Membercount", value="```Show's member's in a server```" , inline = False)
    embed.add_field(name="<:900611921928126484:906858683508600852> Purge", value="```Clear all messages```" , inline = False)
    await ctx.reply(embed = embed)

@slash.slash(description="shows botinfo")
async def botinfo(ctx: SlashContext):
    embed = discord.Embed(title='Bot Information', color=0x2f3136)
    embed.add_field(name='Name', value='```Flank Protection```', inline=False)
    embed.add_field(name='Server Count', value=f'```{len(client.guilds)}```', inline=False)
    embed.add_field(name='User Count', value=f'```{len(set(client.get_all_members()))}```', inline=False)
    embed.add_field(name='Ping', value=f'```{int(client.latency * 1000)}```', inline=False)
    embed.add_field(name='Discord.py', value=f'```1.7.3```', inline=False)
    embed.add_field(name='Creators', value=f'```Sky , Jack ,Ghost And Toxic```', inline=False)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
    await ctx.reply(embed=embed)

@slash.slash(description="shows serverinfo")
async def serverinfo(ctx: SlashContext):
  embed = discord.Embed(title = "Flank Protection Server Info" , color = 0x2f3136)
  embed.add_field(name="Server ID", value=f'```{ctx.guild.id}```', inline=False)
  embed.add_field(name="Server Name", value=f'```{ctx.guild.name}```', inline=False)
  embed.add_field(name="Server Owner", value=f'```{ctx.guild.owner}```', inline=False)
  embed.add_field(name="Creation Date", value=f'```{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}```', inline=False)
  embed.add_field(name="Members", value=f'```{len(ctx.guild.members)}```', inline=False)
  embed.add_field(name="Roles", value=f'```{len(ctx.guild.roles)}```', inline=False)
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.reply(embed = embed)

@slash.slash(description="shows membercount")
async def membercount(ctx: SlashContext):
    embed = discord.Embed(title='Flank Protection Anti Nuke', color=0x2f3136)
    embed.add_field(name="Server Members :", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
    embed.set_footer(text="Flank Protection", icon_url='https://media.discordapp.net/attachments/928254198821310475/953298771113017434/a833aced3a3684a0bd3dc0200ae4a482.png')
    await ctx.reply(embed=embed)

@slash.slash(description="sends bot invite link")
async def invite(ctx):
	embed = discord.Embed(title=f"Invite {client.user.name}", color=0x2f3136, description=f"[Click Here To Invite](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands)")
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands"
				)
			])
		]
	) 

keep_alive()   
client.run(token)
