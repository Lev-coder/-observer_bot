from telegram.ext import Updater

class Sender:

    @staticmethod
    def sendMassage(update: Updater, massageText: str):
        update.message.reply_text(massageText)

    @staticmethod
    def sendMassage(bot, user, massageText: str):
        update = bot.getUpdater()
        bot = update.bot
        bot.send_message(user.chat_id,massageText)