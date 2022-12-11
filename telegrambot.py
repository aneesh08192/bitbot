from logging import Filter
from telegram import chat
from telegram.ext.dispatcher import run_async
from Actress.aishwaryarai import aishwaryarai
from Actress.aliabhatt import aliabhatt
from Actress.amalapaul import amalapaul
from Actress.anasuya import anasuya
from Actress.anjali import anjali
from Actress.anupama import anupama
from Actress.anushkasharma import anushkasharma
from Actress.anushkashetty import anushkashetty
from Actress.asin import asin
from Actress.aunty import aunty
from Actress.bollywood import bollywood
from Actress.charmy import charmy
from Actress.deepikapadukone import deepikapadukone
from Actress.genelia import genelia
from Actress.hansika import hansika
from Actress.ileana import ileana
from Actress.kajal import kajal
from Actress.kajol import kajol
from Actress.kareena import kareena
from Actress.katrina import katrina
from Actress.keerthysuresh import keerthysuresh
from Actress.kiara import kiara
from Actress.kritisanon import kritisanon
from Actress.mouniroy import mouniroy
from Actress.nabha import nabha
from Actress.nayanthara import nayanthara
from Actress.nazriya import nazriya
from Actress.nidhiagarwal import nidhiagarwal
from Actress.nithyamenon import nithyamenon
from Actress.nivetha import nivetha
from Actress.poojahedge import poojahedge
from Actress.privatepics import privatepics
from Actress.priyamani import priyamani
from Actress.priyankachopra import priyankachopra
from Actress.rakul import rakul
from Actress.ramyakrishna import ramyakrishna
from Actress.randompics import randompics
from Actress.rashikanna import rashikanna
from Actress.rashmika import rashmika
from Actress.regina import regina
from Actress.samantha import samantha
from Actress.shraddhakapoor import shraddhakapoor
from Actress.shriyasaran import shriyasaran
from Actress.shruthihassan import shruthihassan
from Actress.sneha import sneha
from Actress.sonarika import sonarika
from Actress.taapsee import taapsee
from Actress.tamanna import tamanna
from Actress.tamilrandom import tamilrandom
from Actress.trisha import trisha
from Actress.urvashirautela import urvashirautela
from Actress.vidhyabalan import vidhyabalan
from Actress.yamigautam import yamigautam
from importsdata import *

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""

        Usage:
              /commad [seconds] [no. Of Images to slide]
        example:
             /kajal 5 10

    """)

def chatauth(update: Update, context: CallbackContext) -> None:
       pass

PORT = int(os.environ.get('PORT', '5000'))
TOKEN = '5135108542:AAGsmFkBgPTvX8TOc_bbLhkydT0fSKjsJFs'
updater = Updater(TOKEN, use_context=True)

#updater.dispatcher.add_handler(MessageHandler(Filters.chat(-351168050),chatauth))
updater.dispatcher.add_handler(CommandHandler('start',start,run_async=True))
updater.dispatcher.add_handler(CommandHandler('aishwaryarai',aishwaryarai,run_async=True))
updater.dispatcher.add_handler(CommandHandler('aliabhatt',aliabhatt,run_async=True))
updater.dispatcher.add_handler(CommandHandler('amalapaul',amalapaul,run_async=True))
updater.dispatcher.add_handler(CommandHandler('anasuya',anasuya,run_async=True))
updater.dispatcher.add_handler(CommandHandler('anjali',anjali,run_async=True))
updater.dispatcher.add_handler(CommandHandler('anupama',anupama,run_async=True))
updater.dispatcher.add_handler(CommandHandler('anushkasharma',anushkasharma,run_async=True))
updater.dispatcher.add_handler(CommandHandler('anushkashetty',anushkashetty,run_async=True))
updater.dispatcher.add_handler(CommandHandler('asin',asin,run_async=True))
updater.dispatcher.add_handler(CommandHandler('aunty',aunty,run_async=True))
updater.dispatcher.add_handler(CommandHandler('bollywood',bollywood,run_async=True))
updater.dispatcher.add_handler(CommandHandler('charmy',charmy,run_async=True))
updater.dispatcher.add_handler(CommandHandler('deepikapadukone',deepikapadukone,run_async=True))
updater.dispatcher.add_handler(CommandHandler('genelia',genelia,run_async=True))
updater.dispatcher.add_handler(CommandHandler('hansika',hansika,run_async=True))
updater.dispatcher.add_handler(CommandHandler('ileana',ileana,run_async=True))
updater.dispatcher.add_handler(CommandHandler('kajal',kajal,run_async=True))
updater.dispatcher.add_handler(CommandHandler('kajol',kajol,run_async=True))
updater.dispatcher.add_handler(CommandHandler('kareena',kareena,run_async=True))
updater.dispatcher.add_handler(CommandHandler('katrina',katrina,run_async=True))
updater.dispatcher.add_handler(CommandHandler('keerthysuresh',keerthysuresh,run_async=True))
updater.dispatcher.add_handler(CommandHandler('kiara',kiara,run_async=True))
updater.dispatcher.add_handler(CommandHandler('kritisanon',kritisanon,run_async=True))
updater.dispatcher.add_handler(CommandHandler('mouniroy',mouniroy,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nabha',nabha,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nayanthara',nayanthara,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nazriya',nazriya,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nidhiagarwal',nidhiagarwal,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nithyamenon',nithyamenon,run_async=True))
updater.dispatcher.add_handler(CommandHandler('nivetha',nivetha,run_async=True))
updater.dispatcher.add_handler(CommandHandler('poojahedge',poojahedge,run_async=True))
updater.dispatcher.add_handler(CommandHandler('privatepics',privatepics,run_async=True))
updater.dispatcher.add_handler(CommandHandler('priyamani',priyamani,run_async=True))
updater.dispatcher.add_handler(CommandHandler('priyankachopra',priyankachopra,run_async=True))
updater.dispatcher.add_handler(CommandHandler('rakul',rakul,run_async=True))
updater.dispatcher.add_handler(CommandHandler('ramyakrishna',ramyakrishna,run_async=True))
updater.dispatcher.add_handler(CommandHandler('randompics',randompics,run_async=True))
updater.dispatcher.add_handler(CommandHandler('rashikanna',rashikanna,run_async=True))
updater.dispatcher.add_handler(CommandHandler('rashmika',rashmika,run_async=True))
updater.dispatcher.add_handler(CommandHandler('regina',regina,run_async=True))
updater.dispatcher.add_handler(CommandHandler('samantha',samantha,run_async=True))
updater.dispatcher.add_handler(CommandHandler('shraddhakapoor',shraddhakapoor,run_async=True))
updater.dispatcher.add_handler(CommandHandler('shriyasaran',shriyasaran,run_async=True))
updater.dispatcher.add_handler(CommandHandler('shruthihassan',shruthihassan,run_async=True))
updater.dispatcher.add_handler(CommandHandler('sneha',sneha,run_async=True))
updater.dispatcher.add_handler(CommandHandler('sonarika',sonarika,run_async=True))
updater.dispatcher.add_handler(CommandHandler('taapsee',taapsee,run_async=True))
updater.dispatcher.add_handler(CommandHandler('tamanna',tamanna,run_async=True))
updater.dispatcher.add_handler(CommandHandler('tamilrandom',tamilrandom,run_async=True))
updater.dispatcher.add_handler(CommandHandler('trisha',trisha,run_async=True))
updater.dispatcher.add_handler(CommandHandler('urvashirautela',urvashirautela,run_async=True))
updater.dispatcher.add_handler(CommandHandler('vidhyabalan',vidhyabalan,run_async=True))
updater.dispatcher.add_handler(CommandHandler('yamigautam',yamigautam,run_async=True))

updater.start_polling()
#updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN,webhook_url="https://captainrodsparrws.herokuapp.com/" + TOKEN)
updater.idle()
