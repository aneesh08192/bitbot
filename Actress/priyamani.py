from importsdata import * 

def priyamani(update: Update, context: CallbackContext) -> None:
    x = priyamani_list[randrange(0,len(priyamani_list))]
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
        x = priyamani_list[randrange(0,len(priyamani_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

priyamani_data = """https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-049.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-036.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-042.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-014.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-024.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-052.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-053.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-016.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-025.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-065.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-Tamil-Actress-Sex-003.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-001.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-059.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-006.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-038.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-Tamil-Actress-Sex-002.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-031.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-009.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-021.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-039.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-048.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-061.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-022.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-013.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-045.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-015.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-057.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-017.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-002.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-034.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-032.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-046.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-041.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-012.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-004.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-Tamil-Actress-Sex-004.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-019.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-029.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-044.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-051.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-010.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-028.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-054.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-030.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-027.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-Tamil-Actress-Sex-006.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-058.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-037.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-011.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-020.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-040.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-043.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-007.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-026.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-023.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-005.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-035.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-003.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-060.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-008.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-033.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-Tamil-Actress-Sex-005.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-047.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-055.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-063.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-050.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-064.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-062.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-056.jpg
https://img.freefake.work/images/2020/07/03/Priyamani-Nude-South-Indian-Actress-Sex-018.jpg"""

global priyamani_list
priyamani_list = priyamani_data.splitlines()

