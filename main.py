import telebot
from datasets import *

def nalog1(pay):
    return str(pay * 0.06)


def nalog2(take, give):
    return str((take - give) * 0.15)


def nalog3(k1, k2, rab_amount, bd):
    return str(k1 * k2 * rab_amount * bd * 0.15)


def nalog4(fiksa):
    return str(fiksa * 0.06)


def GetEffectiveWork(id):
    print(data[id][1])
    print(data[id][18])
    print(data[id][4])
    if data[id][1] == "Москва и Московская обл.":
        if data[id][18] == "Да, менее 2.4 млн":
            if data[id][4] == "Один":
                return "Самозанятый, т.к. Ваш город Москва, доход менее 2.4 млн рублей в год и отсутствуют наемный работники"
    if data[id][29] == "Да, собираюсь" or data[id][7] == "Нет, будут другие":
        return "ООО, т.к. у Вас несколько учередителей или Вы хотите сотрудничать с гос. учереждениями"
    return "ИП"


def tern(id):
    if data[id][3] == 'Парикмахерские и косметические услуги':
        return 900000
    return 600000


def GetEffectiveTax(id):
    if GetEffectiveWork(id) == "Самозанятый, т.к. Ваш город Москва, доход менее 2.4 млн рублей в год и отсутствуют наемные работники":
        if data[id][19] == "Нет, не буду":
            return 0.04
        else:
            return 0.06
    else:
        if GetEffectiveWork(id) == "ИП":
            if int(data[id][5]) < 16:
                if data[id][22] == "Да, является":
                    return 0.06 * tern(id) * int(data[id][23]) / 12
        return 0.04



number = {}
data = {}

token = '887201975:AAFxeddwHvOSnQ-hEUIB88cuQo5i320Hb1I'

bot = telebot.TeleBot(token)

def TaxForSlaves(pay):
    return pay * 0.302

def govno(id):
    line = "Моя работа на этом закончена.\n"
    line += "Наилучший вариант: " + GetEffectiveWork(id) + '\n'
    line += "Возможный вариант заплатить налог: " + str(GetEffectiveTax(id) * 100) + '%\n'
    line += "В размере: " + str(GetEffectiveTax(id) * int(data[id][30])) + '\n\n'
    line += "Другие налоговые ставки, рассчитанные на основании введенных Вами данных:\n"
    if data[id][11] == "Нет, менее или отсутствуют" and data[id][12] == "Нет, не имеет":
        line += "УСНД: " + nalog1(int(data[id][30])) + '\n'
        line += "УСНДР: " + nalog2(int(data[id][30]), int(data[id][31])) + '\n'
    ddd = data[id]
    if data[id][5] != "Один" and data[id][12] == "Нет, не имеет":
        line += "ЕНВД: " + nalog3(1.798, 1, int(data[id][5]), 7500 * 12) + '\n' + "ПВД: " + nalog4(356400)
    else:
        line += "ЕНВД: " + nalog3(1.798, 1, 1, 7500 * 12) + '\n' + "ПВД: " + nalog4(356400)
    if data[id][28] == "Да":
        line += "\nЕСХН: " + str((int(data[id][30])-int(data[id][31]))*0.06)
        line += "\nТакже в год Вам необходимо заплатить взносы за сотрудников в размере: " + str(TaxForSlaves(int(data[id][31])))
    if GetEffectiveWork(id) == "ИП":
        line += "\nТак как Вы являетесь ИП, Вы должны заплатить страховой взнос в размере 36238 рублей, если Ваш доход не привысил 300000 рублей." \
                "\nЕсли Вы нанимаете сотрудников, то Вы также должны заплатить " + str(TaxForSlaves(int(data[id][31])))
    return line

#@bot.message_handler(content_types=['text'])
def send_text(message):
    id = message.chat.id
    if id not in number.keys():
        number[id] = 0
        data[id] = {}
    previd = number[id]
    if number[id] == len(questions):
        number.pop(id)
        bot.send_message(id, govno(id))
        ddd = data[id]
        a = 5
        a += 1
        return
    if number[id] == 4 and message.text == "Один":
        number[id] = 6
        data[id][5] = 1
    if number[id] == 8 and message.text == "Нет, не нужно":
        number[id] = 9
        data[id][8] = 999999999999999
    if number[id] == 22 and message.text == "Нет, не является":
        number[id] = 23
    if number[id] == 24 and message.text == "Да":
        number[id] = 26
    if number[id] == 25 and message.text == "Нет, не было":
        number[id] = 26
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    if number[id] == 0:
        for i in regs.keys():
            keyboard1.row(i)
        bot.send_message(id, questions[number[id]], reply_markup=keyboard1)
    elif number[id] == 1:
        for i in regs[message.text]:
            keyboard1.row(i)
        bot.send_message(id, questions[number[id]], reply_markup=keyboard1)
    elif number[id] == 2:
        for i in types:
            keyboard1.row(i)
        bot.send_message(id, "Хей, я вижу, ты решил открыть бизнес в городе " + message.text + "!\n" + questions[number[id]], reply_markup=keyboard1)
    else:
        keyboard1.row(values[number[id]][0], values[number[id]][1])
        if values[number[id]][0] == "":
            bot.send_message(id, questions[number[id]])
        else:
            bot.send_message(id, questions[number[id]], reply_markup=keyboard1)
    data[id][previd] = message.text
    number[id] += 1

if __name__ == '__main__':
    print("ffff")
    bot.send_message(84367486, "Hello world")
    #bot.polling(none_stop=True)


