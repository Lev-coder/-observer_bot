from telegram.ext import Updater

class Sender:

    @staticmethod
    def sendMassage(update: Updater, massageText: str):
        update.message.reply_text(massageText)

    @staticmethod
    def sendMassageByBot(bot, user, massageText: str):
        bot.sendMessage(user,massageText)