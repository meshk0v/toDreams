import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton(text="добавить задачу", callback_data="first")
    item2 = types.InlineKeyboardButton(text="список задач", callback_data="second")
    item3 = types.InlineKeyboardButton(text="о боте",callback_data="tri")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    sent = bot.send_message(message.chat.id, "выберите действие", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "back":

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton(text="добавить задачу", callback_data="first")
        item2 = types.InlineKeyboardButton(text="список задач", callback_data="second")
        item3 = types.InlineKeyboardButton(text = "о боте", callback_data="tri")
        markup.add(item1)
        markup.add (item2)
        markup.add(item3)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="выберите действие",reply_markup=markup)

    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        #rele1 = types.InlineKeyboardButton(text="1t", callback_data="1")
        #rele2 = types.InlineKeyboardButton(text="2t", callback_data="2")
        #rele3 = types.InlineKeyboardButton(text="3t", callback_data="3")
        backbutton = types.InlineKeyboardButton(text="назад", callback_data="back")
        keyboard.add(backbutton)
        sent = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="введите задачу",reply_markup=keyboard)
        bot.register_next_step_handler(sent,get2)
    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="назад", callback_data="back")
        #backbutton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        keyboard.add(rele1)
        sent = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="список задач",reply_markup=keyboard)
        bot.register_next_step_handler(sent,get1)
    elif call.data == "tri":
        keyboard = types.InlineKeyboardMarkup()
        back1 = types.InlineKeyboardButton(text="назад", callback_data="back")
        keyboard.add(back1)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Каждый день ты ставишь себе цели на день, как правило, цели, которые ты ставишь приближают тебя к какой-то великой цели или мечте. И этот бот помогает тебе добиться твоей главной цели. В Бот ты пишешь ежедневно задачи, которые тебе нужно выполнить для реализации основной цели, бот в определённый период времени напоминает тебе о задачах, которые ты поставил себе на день, и если вдруг ты замотался и забыл про задачи, или ТикТок и подобные соц сети яро поглотили твое внимание,бот с радостью уведомить о том, что у тебя есть невыполненные задачи и тебе скорее нужно бросить все неважные дела и работать над основными задачами",reply_markup=keyboard)
    elif call.data == "1" or call.data == "2" or call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="")
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="lastlayer", callback_data="ll")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="last layer",reply_markup=keyboard3)
    elif call.data == 'yes':
        keyboard3 = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Задача была выполнена. Поздравляю",reply_markup=keyboard3)
    elif call.data == 'no':
        keyboard3 = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "Задача не была выполнена(",reply_markup=keyboard3)

#@bot.callback_query_handler(lambda c: call.data == 'second')
@bot.message_handler(func=lambda call: True)
def get1(message):
    #if call.date == 'second':
        #markup = types.InlineKeyboardMarkup()
        #item1 = types.InlineKeyboardButton(text='✅', callback_data='yes')
        #item2 = types.InlineKeyboardButton(text='❌', callback_data='no')
        #markup.add(item1,item2)
    bot.send_message(message.chat.id, f"{message.text}")

@bot.message_handler(func=lambda call: True)
def get2(message):
    #if call.date == 'second':
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='✅', callback_data='yes')
        item2 = types.InlineKeyboardButton(text='❌', callback_data='no')
        markup.add(item1,item2)
        bot.send_message(message.chat.id, f"{message.text}")





#@bot.message_handler(func=lambda call: True)
#def get_title(message):
#    data = message.text
#    markup = types.InlineKeyboardMarkup()
#    item1 = types.InlineKeyboardButton(text='✅', callback_data='yes')
#    item2 = types.InlineKeyboardButton(text='❌', callback_data='no')
#    markup.add(item1,item2)
#    bot.send_message(message.chat.id, f"{message.text}",reply_markup=markup)

#@bot.callback_query_handler(func=lambda call: True)
#def callback_handler(call):
#    if call.data == 'yes':
#        bot.send_message(call.message.chat.id, 'Задача была выполнена. Поздравляю')

#    elif call.data == 'no':
#        bot.send_message(call.message.chat.id, 'Задача была удалена')

#if __name__ == "__main__":
bot.polling(none_stop=True)



