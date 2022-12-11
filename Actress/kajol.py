from importsdata import * 

def kajol(update: Update, context: CallbackContext) -> None:
    x = kajol_list[randrange(0,len(kajol_list))]
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
        x = kajol_list[randrange(0,len(kajol_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

kajol_data = """https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-003.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-045.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-072.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-108.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-112.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-042.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-100.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-5.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-103.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-027.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-022.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-007.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-11.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-110.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-060.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-1.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-044.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-024.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-111.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-078.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-29.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-037.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-004.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-012.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-10.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-034.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-053.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-22.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-36.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-089.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-24.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-083.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-033.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-27.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-32.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-026.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-096.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-051.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-043.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-31.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-084.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-13.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-032.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-070.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-30.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-018.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-114.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-18.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-008.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-7.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-35.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-047.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-092.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-061.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-40.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-081.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-039.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-9.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-33.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-068.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-036.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-16.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-098.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-005.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-075.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-12.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-038.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-054.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-014.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-023.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-26.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-088.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-41.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-010.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-017.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-035.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-021.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-065.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-025.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-066.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-067.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-049.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-058.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-34.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-20.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-050.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-020.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-001.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-109.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-095.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-046.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-048.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-19.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-3.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-016.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-082.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-080.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-079.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-056.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-063.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-117.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-028.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-093.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-097.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-041.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-019.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-064.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-104.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-4.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-029.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-055.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-099.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-040.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-059.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-116.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-057.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-086.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-38.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-052.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-077.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-009.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-28.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-006.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-105.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-094.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-074.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-39.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-085.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-8.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-062.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-071.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-25.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-013.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-14.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-091.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-102.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-15.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-115.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-113.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-101.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-087.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-015.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-030.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-6.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-106.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-031.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-2.png
https://img.freefake.work/images/2020/07/03/Kajol-Nude-Indian-actress-Sex-23.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-076.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-090.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-069.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-073.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-107.jpg
https://img.freefake.work/images/2020/07/03/Kajol-Devgan-Nude-Indian-film-actress-Sex-011.jpg"""

global kajol_list
kajol_list = kajol_data.splitlines()

