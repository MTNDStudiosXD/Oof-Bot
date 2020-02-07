import discord
import datetime
import random
import asyncio
import time
import keep_alive
import os
#------------------------------------
from discord.ext import *
from discord.ext import commands
#-------------------------------------

print("Bot loading...")

bot = commands.Bot(command_prefix=':!') #prefix
 #removes a automatic help command that generates itself.

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name=":!help", url="https://www.twitch.tv/oof"))
  print(f"Bot is online!") # Shows on the console that the bot is working.
    

@bot.command(pass_context=True) 
async def serverstatus(ctx):
  print ("Replying")
  await ctx.send("**Loading... 🔃**")

  await ctx.send("**Checking Status... ⚠**")




  await ctx.send("**Checking Server LOGS... 🧱**")




  await ctx.send("**Checking Online, Offline Users... 📱💻**")





  await ctx.send("**Connecting to Server... 📛**")






  await ctx.send("**Located Server, Connecting... 📶**")





  await ctx.send("**Server Speed: 0 📊**")





  await ctx.send("**Server Hosted By: ÑightSG👻🐱‍👤**")





  await ctx.send("**(C) ÑightSG, 2020**")




  await ctx.send("**Collecting Server Information... 📝**")




  

  await ctx.send ("**Checking Server DATA-BASES... 🎃**")


  await ctx.send ("**Connected to server! 🤘**")


  await ctx.send ("```ServerStatus: DOWN.```")


  await ctx.send ("||Note: This Plugin MAY Not Work at All Times||")

@bot.command(pass_context=True)
async def deposit(ctx):
  print ("Replying...")
  await ctx.send("Loading... 🔃")
  await ctx.send("No Current Deposit World.")

@bot.command(pass_context=True) 
async def email(ctx):
  print ("Replying...")
  await ctx.send("Loading... 🔃")
  await ctx.send("No Current GTVF Email.")

keep_alive.keep_alive()
token = os.environ.get("BOT_TOKEN_HERE")
bot.run(proccess.env.token) 
