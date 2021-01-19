from nonebot.log import logger
from game.utils.database import *
from game.config import *
from game.utils.avatar import *
# 服务器类
class Server:
  def __init__(self):
    self.start()
    self.global_dict = {
      "in_game" : False
    }

  # 服务器启动逻辑
  def start(self):
    logger.info("PSL启动!")
    if PICTURE_MODE:
      logger.info("当前模式：图片模式")
    else:
      logger.info("当前模式：文字模式")
  
    #download_avatars()
    

  def close(self):
    logger.info("PSL关闭!")

  def get(self,key):
    return self.global_dict[key]

  def set(self,key, value):
    self.global_dict[key] = value

# 全局服务器
g_server = Server()
