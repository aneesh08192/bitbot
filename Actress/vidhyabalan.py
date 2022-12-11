from importsdata import * 

def vidhyabalan(update: Update, context: CallbackContext) -> None:
    x = vidhyabalan_list[randrange(0,len(vidhyabalan_list))]
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
        x = vidhyabalan_list[randrange(0,len(vidhyabalan_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

vidhyabalan_data = """https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-22.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16374.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16359.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16392.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16456.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16480.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-19.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16368.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16427.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-15.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-32.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-11.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16414.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16471.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16478.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16485.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-8.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16451.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16442.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-42.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16443.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16444.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16469.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16487.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16413.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16373.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-1.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16370.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-43.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16447.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16407.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16425.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16423.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16419.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-14.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-17.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16422.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16489.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16412.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-34.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16364.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16461.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16418.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16458.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16393.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16473.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16477.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16440.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16466.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16406.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16430.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-24.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-44.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16381.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16411.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16462.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16463.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16464.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16410.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16446.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-25.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16428.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16395.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16409.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16426.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16445.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16361.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16424.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-18.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16379.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16474.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16397.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-35.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16432.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16387.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16457.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16378.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16421.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-12.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16383.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-16.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16391.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16394.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16492.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-33.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16396.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16375.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-30.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16488.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-36.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-7.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16491.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16482.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16382.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16453.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-10.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-9.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16465.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16404.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16363.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16433.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-23.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16450.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16439.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16372.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16460.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16402.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16437.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-38.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-41.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16479.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16385.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-5.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-13.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-29.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16470.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16362.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-20.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16389.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-39.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-21.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16420.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16400.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16486.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16360.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16376.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16438.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-28.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16475.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16377.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16408.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16380.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16384.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16436.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16467.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16435.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-27.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-6.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16390.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16472.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16483.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16403.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16369.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16484.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16459.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16431.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-31.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16365.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16452.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16401.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16398.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-2.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16481.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-26.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-46.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16448.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-45.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16415.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16388.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16429.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16454.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-3.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16358.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16386.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-actress-Sex-40.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16399.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16405.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16434.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16371.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16455.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16468.jpg
https://img.freefake.work/images/2020/07/03/Vidya-Balan-Nude-Indian-Actress-Sex-16441.jpg"""

global vidhyabalan_list
vidhyabalan_list = vidhyabalan_data.splitlines()

