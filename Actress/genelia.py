from importsdata import * 

def genelia(update: Update, context: CallbackContext) -> None:
    x = genelia_list[randrange(0,len(genelia_list))]
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
        x = genelia_list[randrange(0,len(genelia_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

genelia_data = """https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5242.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5295.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5289.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-6.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-16.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-15.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5290.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5259.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5281.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-10.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5249.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5288.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5235.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5305.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5267.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5236.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5258.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-14.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5246.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5244.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5296.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-7.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-20.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5279.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5247.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5248.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5231.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5261.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-24.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5297.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5300.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5237.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5233.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5234.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5264.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-12.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5287.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5298.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5303.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5240.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5232.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5302.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-5.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5301.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-22.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5250.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-1.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-11.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5245.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5241.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-19.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5285.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5304.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5284.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-8.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5262.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5282.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-3.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5238.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5286.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5291.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-9.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5239.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-4.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5275.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5266.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-13.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-17.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5263.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-21.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-2.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-23.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5243.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-film-actress-Sex-5299.jpg
https://img.freefake.work/images/2020/07/03/Genelia-Nude-Indian-actress-Sex-18.jpg"""

global genelia_list
genelia_list = genelia_data.splitlines()

