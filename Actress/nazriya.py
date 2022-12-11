from importsdata import * 

def nazriya(update: Update, context: CallbackContext) -> None:
    x = nazriya_list[randrange(0,len(nazriya_list))]
    try:
        msg = update.message.reply_photo(str(x))
    except:
        msg = update.message.reply_photo(str(x))
    logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    if(len(context.args) != 2):
        time_space = '5'
        images = 0
    else: 
        time_space = context.args[0]
        images = int(context.args[1])
        if int(time_space) < 0:
            time_space = '5'

    time.sleep(int(time_space))

    for image in range(0,images):
        x = nazriya_list[randrange(0,len(nazriya_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

nazriya_data = """https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-4.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12172.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12168.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12235.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12184.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12200.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12233.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12229.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12189.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12152.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12199.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-7.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12178.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-1.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-3.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12194.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12156.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12198.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12135.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12179.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12161.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12165.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12185.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12138.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12196.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12193.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12148.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12160.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12157.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12239.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12146.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-6.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12169.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12219.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12202.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-11.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12215.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12207.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12182.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12249.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12139.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12230.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12142.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12214.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12232.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12197.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12158.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12144.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12166.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12175.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12186.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12164.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12173.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12210.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-10.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12145.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12213.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12155.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12237.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12180.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12141.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-8.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12227.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12191.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-9.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12143.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12212.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12206.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12217.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12140.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12236.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12183.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12205.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12190.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12231.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12211.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12223.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12159.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12238.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12208.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12134.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12251.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12187.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12248.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12153.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12188.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12147.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12137.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12174.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12209.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12162.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12151.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12246.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12195.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12203.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-2.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12204.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12154.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12218.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12192.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12171.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-South-Indian-actress-Sex-5.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12167.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12250.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12150.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12149.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12170.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12224.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12163.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12176.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12181.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12136.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12216.jpg
https://img.freefake.work/images/2020/07/03/Nazriya-Nazim-Nude-Malayalam-actress-Sex-12201.jpg"""

global nazriya_list
nazriya_list = nazriya_data.splitlines()

