import discord
from discord.ext import commands
import random
import keep_alive
import os

normal_amount = len(os.listdir("./卡包"))
special_amount = len(os.listdir("./特典"))
tft_amount = len(os.listdir("./姆咪戰棋"))
carddd_amount = len(os.listdir("./carddd"))
mbti_amount = len(os.listdir("./mbti"))

card = commands.Bot(command_prefix='~')  #定義為一個bot


@card.event
async def on_ready():  #重新定義on_ready
    print(">>啟動成功<<")

    channel = card.get_channel(961913026024448010)
    channel = card.get_channel(1159056138894065666)

    print(normal_amount)
    print(special_amount)
    print(tft_amount)
    print(carddd_amount)
    print(mbti_amount)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def 讓我抽抽(ctx):
    random_nk338 = random.randint(1, normal_amount)
    nk338 = discord.File("卡包/%d.png" % random_nk338)
    await ctx.send(file=nk338)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def 特(ctx):
    random_special = random.randint(1, special_amount)
    special = discord.File("特典/A%d.png" % random_special)
    await ctx.send(file=special)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def TFT(ctx):
    random_tft = random.randint(1, tft_amount)
    tft = discord.File("姆咪戰棋/B%d.png" % random_tft)
    await ctx.send(file=tft)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def 卡一個(ctx):
    random_carddd = random.randint(1, carddd_amount)
    carddd = discord.File("carddd/C%d.png" % random_carddd)
    await ctx.send(file=carddd)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def mbti(ctx):
    random_mbti = random.randint(1, mbti_amount)
    mbti = discord.File("mbti/m%d.jpg" % random_mbti)
    await ctx.send(file=mbti)


@commands.cooldown(1, 10, commands.BucketType.user)
@card.command()
async def reload(ctx):
    reload_carkpacks()
    await ctx.reply("成功刷新卡包")


def reload_carkpacks():
    global normal_amount
    global special_amount
    global tft_amount
    global carddd_amount
    global mbti_amount

    normal_amount = len(os.listdir("./卡包"))
    special_amount = len(os.listdir("./特典"))
    tft_amount = len(os.listdir("./姆咪戰棋"))
    carddd_amount = len(os.listdir("./carddd"))
    carddd_amount = len(os.listdir("./mbti"))

    print(normal_amount)
    print(special_amount)
    print(tft_amount)
    print(carddd_amount)
    print(mbti_amount)


keep_alive.keep_alive()
card.run(
    "放你的Discord Token")
