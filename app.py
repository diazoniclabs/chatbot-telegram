from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client, Data
aio = Client('Diazonic', 'bb69d720de4446128cbbf7bcae1531a4')

def demo_on(bot,update):
  data = Data(value=1)
  aio.create_data('light', data)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned on')
  update.bot.sendPhoto(chat_id=chat_id,photo='https://static.scientificamerican.com/sciam/cache/file/2B38DE31-C1D3-4339-8808D61972976EE4.jpg',caption="light on")

def demo_off(bot,update):
  data = Data(value=0)
  aio.create_data('light', data)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned off')
  update.bot.sendPhoto(chat_id=chat_id,photo='https://image.shutterstock.com/image-photo/light-bulb-turned-off-over-260nw-320485652.jpg',caption="light off")

def demo(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Wrong input')
  

def main(bot,update):
  a = bot.message.text.lower()
  if a == "light on":
    demo_on(bot,update)
  elif a == "light off":
    demo_off(bot,update)
  else:
    demo(bot,update)


bot_token = '2063969554:AAHevamQ5VGx_WdXLNhEC1hMI8_XQHo_2Kg'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
