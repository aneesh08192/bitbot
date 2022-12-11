from importsdata import * 

def nithyamenon(update: Update, context: CallbackContext) -> None:
    x = nithyamenon_list[randrange(0,len(nithyamenon_list))]
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
        x = nithyamenon_list[randrange(0,len(nithyamenon_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

nithyamenon_data = """https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8423.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8406.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8397.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8405.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8414.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8340.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8365.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8367.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8377.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8426.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8369.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8359.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8382.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8358.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8352.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8425.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8391.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8400.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8378.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8409.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8344.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8374.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8401.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8371.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8355.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8408.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8362.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8416.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8357.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8348.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8385.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8424.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8412.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8375.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8342.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8387.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8396.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8376.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8381.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8403.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8420.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8373.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8384.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8407.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8360.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8388.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8363.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8379.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8427.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8389.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8346.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8356.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8350.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8390.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8417.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8415.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8361.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8419.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8341.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8354.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8366.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8422.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8386.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8351.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8410.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8383.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8343.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8398.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8399.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8353.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8404.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8345.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8413.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8402.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8372.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8421.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8394.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8380.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8393.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8418.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8395.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8411.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8368.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8370.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8364.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8349.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8392.jpg
https://img.freefake.work/images/2020/07/03/Nithya-Menen-Nude-Malayalam-Actress-Sex-8347.jpg"""

global nithyamenon_list
nithyamenon_list = nithyamenon_data.splitlines()

