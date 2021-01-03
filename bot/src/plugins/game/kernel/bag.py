import random
import math
from nonebot import on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from game.utils.database import *
from game.model.user import *
from game.model.player import *
from game.model.bag import *
from game.kernel.account import check_account
from game.utils.image import toImage

user_bag = on_startswith(msg="背包", rule=to_me(), priority=1)


@user_bag.handle()
async def user_bag_handler(bot: Bot, event: Event, state: dict):
    arg = str(event.message).split(" ")
    user = await check_account(user_bag, event)
    bag = Bag.getBag(user)
    if (len(arg) == 1):
        await get_bag_by_page(bag, "1")
    elif len(arg) == 3:
      if arg[1] == "查询":
        await query_bag(bag, arg[2])
      else:
        await user_bag.finish("参数错误", **{"at_sender": True})
        return
    else:
        page = arg[1]
        if not page.isdecimal():
            await user_bag.finish("参数错误", **{"at_sender": True})
            return
        await get_bag_by_page(bag, page)


async def get_bag_by_page(bag: Bag, page: str):
    if bag == None:
      await user_bag.finish("当前背包为空", **{"at_sender":True})
    total_page = math.ceil(len(bag.cards) / 20)
    page = int(page)
    if page > total_page or page <= 0:
        await user_bag.finish("页码错误", **{"at_sender": True})
        return

    ret = ""
    if (bag != None):
        for i in range(20):
            index = (page - 1) * 20 + i
            if index >= len(bag.cards):
                break
            card = bag.cards[index]
            ret += "[" + str(card.id) + "]\t"
            ret += card.format()
            ret += "\n"
    foot = "第" + str(page) + "页 共" + str(total_page) + "页\n输入“背包 页码”跳转到指定页\n"
    foot += "输入“背包 查询 球员名”查找同名球员卡\n"
    foot += "输入“球员 ID”查看详细信息"
    await user_bag.finish("当前背包：\n" + toImage(ret+foot), **{"at_sender": True})

async def query_bag(bag, name):
    ret = ""
    if bag != None:
      for card in bag.cards:
        if name.lower() in card.player.Name.lower():
          ret += "[" + str(card.id) + "]\t"
          ret += card.format()
          ret += "\n"
    foot = "输入“背包 查询 球员名”查找同名球员卡\n"
    foot += "输入“球员 ID”查看详细信息"
    await user_bag.finish("当前背包：\n" + toImage(ret+foot), **{"at_sender": True})