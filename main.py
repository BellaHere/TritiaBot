import discord

from discord.ext import commands

import json
import asyncio
import random
import os


client = discord.Client()

PREFIX = ("t!")

bot = commands.Bot(command_prefix="t!")

#Got the prefix from stack overflow.





@client.event
async def on_ready():
  print('We are online baby!')
#Code from Lucas and FreeCodeCamp.org on Youtube, both work, for simplicity I will be using Lucas's code.










@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.name}#{member.discriminator}.')


@bot.command()
async def unban(ctx, *, member):
  banned_users = ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator)  == (member_name, member_discriminator):
      await ctx.guild.unabn(user)
      await ctx.send(f'Unbanned {user.name}#{user.discriminator}.')
      return
      
#Code from Lucas on youtube.









try:
    with open("users.json") as fp:
        users = json.load(fp)
except Exception:
    users = {}

def save_users():
    with open("users.json", "w+") as fp:
        json.dump(users, fp, sort_keys=True, indent=4)

def add_points(user: discord.User, points: int):
    id = user.id
    if id not in users:
        users[id] = {}
    users[id]["points"] = users[id].get("points", 0) + points
    print("{} now has {} points".format(user.name, users[id]["points"]))
    save_users()

def get_points(user: discord.User):
    id = user.id
    if id in users:
        return users[id].get("points", 0)
    return 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("{} sent a message".format(message.author.name))
    if message.content.lower().startswith("t!lvl"):
        message = "You have {} points!".format(get_points(message.author))
        await client.process_commands(message.channel, msg)
    add_points(message.author, 1)

#Think I found this somewhere on stack overflow.










@bot.command()
async def balance(ctx):
  open_account(ctx.author)
  user = ctx.author
  users = get_bank_data()

  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  
  em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Colour.green())
  em.add_field(name = "Wallet",value = wallet_amt)
  em.add_field(name = "Bank",value= bank_amt)
  await ctx.send(embed = em)




@bot.command()
async def beg(ctx):
  open_account(ctx.author)
  
  user = ctx.author
  
  users = get_bank_data()
  

  earnings = random.randrange(101)

  
  await ctx.send(f"Someone gave you {earnings} coins.")

  
  users[str(user.id)]["wallet"] += earnings
 
  with open("money.json", "w") as f:
    json.dump(users, f)




@bot.command()
async def work(ctx):
  open_account(ctx.author)
  
  user = ctx.author
  
  users = get_bank_data()
  

  earnings = random.randrange(501)

  
  await ctx.send(f"You actually did your job and got {earnings} coins.")

  
  users[str(user.id)]["wallet"] += earnings
 
  with open("money.json", "w") as f:
    json.dump(users, f)




@bot.command()
async def search(ctx):
  open_account(ctx.author)
  
  user = ctx.author
  
  users = await get_bank_data()
  

  earnings = random.randrange(101)

  
  await ctx.send(f"You searched for money and got {earnings} coins.")

  
  users[str(user.id)]["wallet"] += earnings
 
  with open("money.json", "w") as f:
    json.dump(users, f)



  
def open_account(user):
    users = get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)
    return True


                                



def get_bank_data():
    with open("money.json", "r") as f:
      users = json.load(f)

    return users






  
#This code is from Code with Swastik on Youtube, his video on economy bots.




client.run(os.getenv('TOKEN'))