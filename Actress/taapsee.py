from importsdata import * 

def taapsee(update: Update, context: CallbackContext) -> None:
    x = taapsee_list[randrange(0,len(taapsee_list))]
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
        x = taapsee_list[randrange(0,len(taapsee_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

#    msg.delete()

taapsee_data = """https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6054.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6102.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5996.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6004.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6069.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6051.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6001.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6002.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6124.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5999.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6100.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6063.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5980.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5985.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6067.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5998.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6044.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6073.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5990.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6016.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5997.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6057.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6009.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6121.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6090.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6047.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6108.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6052.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6089.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6018.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6107.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6064.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6060.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6071.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6024.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6123.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6126.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6072.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6012.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6129.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6082.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6075.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6029.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6011.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6106.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6127.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6091.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6125.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6066.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6122.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6114.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6099.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5986.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6027.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6038.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6049.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5991.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5983.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6065.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6058.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6040.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6104.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6005.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6006.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6085.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5988.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6003.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5993.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6078.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6043.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5995.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5982.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6068.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5981.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6119.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6128.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5989.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6007.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6053.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6094.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6095.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6010.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6025.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6109.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6105.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5992.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6116.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6021.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6019.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6022.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6117.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6059.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6000.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6093.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5994.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6017.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6083.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5984.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6113.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6056.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6039.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6050.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6032.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6110.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6046.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6120.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6055.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6045.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6103.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6014.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6070.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6062.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6080.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6111.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6013.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6037.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6076.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6074.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6008.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6028.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6061.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-5987.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6081.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6112.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6115.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6088.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6079.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6092.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6084.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6020.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6036.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6097.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6015.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6048.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6042.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6023.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6098.jpg
https://img.freefake.work/images/2020/07/03/Taapsee-Pannu-Nude-Indian-Actress-Sex-6101.jpg"""

global taapsee_list
taapsee_list = taapsee_data.splitlines()

