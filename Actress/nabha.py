from importsdata import * 

def nabha(update: Update, context: CallbackContext) -> None:
    x = nabha_list[randrange(0,len(nabha_list))]
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
        x = nabha_list[randrange(0,len(nabha_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

   # msg.delete()

nabha_data = """https://imgfy.net/images/2020/07/23/Pics-Art-07-17-09-04-31.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-57-26.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-43-45.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-33-47.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-31-44.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-24-14.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-18-05.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-11-21.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-08-03-25.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-17-07-55-02.jpg
https://imgfy.net/images/2020/07/23/Pics-Art-07-16-08-04-30.jpg
https://imgfy.net/images/2020/07/06/NabhaNatesh100596.jpg
https://imgfy.net/images/2020/07/06/5a0832402a10e6e31.jpg
https://imgfy.net/images/2020/07/06/48bcf9d41d88ed86e.jpg
https://imgfy.net/images/2020/07/06/3fecd16da76727ca5.jpg
https://imgfy.net/images/2020/07/06/13c30444be7099561.jpg
https://imgfy.net/images/2020/07/06/22f77fff8dfc4eaf8.jpg
https://imgfy.net/images/2020/07/06/NabhaNatesh100595.jpg
https://imgfy.net/images/2020/07/06/NabhaNateshKriti100594.jpg
https://imgfy.net/images/2020/07/06/Nabha-3b25a093490e354a6.jpg
https://imgfy.net/images/2020/07/06/Nabha-4dba1dc08072372cc.jpg
https://imgfy.net/images/2020/07/06/Nabha-2fda3f541fe4e91b7.jpg
https://imgfy.net/images/2020/07/06/Nabha-179244b8cb8d6401d.jpg
https://imgfy.net/images/2020/07/06/5b0fe23a51711d8c5.jpg
https://imgfy.net/images/2020/07/06/473dbd1297a503f75.jpg
https://imgfy.net/images/2020/07/06/3d9b3fcbc679df4e9.jpg
https://imgfy.net/images/2020/07/06/264760b9d0b7fc524.jpg
https://imgfy.net/images/2020/07/06/12c80546be0693f7c.jpg
https://imgfy.net/images/2020/07/06/nabha-natesh-ass-fucking000554.jpg
https://imgfy.net/images/2020/07/06/4cee3a959e87eaee0.jpg
https://imgfy.net/images/2020/07/06/3b791ecf62992a8c8.jpg
https://imgfy.net/images/2020/07/06/2eb694e023370870f.jpg
https://imgfy.net/images/2020/07/06/11c85b91e557663f9.jpg
https://imgfy.net/images/2020/07/06/Nabha-5.jpg
https://imgfy.net/images/2020/07/06/Nabha-3.jpg
https://imgfy.net/images/2020/07/06/Nabha-4.jpg
https://imgfy.net/images/2020/07/06/Nabha-1.jpg
https://imgfy.net/images/2020/07/06/Nabha-2.jpg
https://imgfy.net/images/2020/07/06/PicsArt_07-05-03.45.18.jpg
https://imgfy.net/images/2020/07/06/PicsArt_07-05-03.46.08.jpg
https://imgfy.net/images/2020/07/06/PicsArt_07-05-03.46.47.jpg
https://imgfy.net/images/2020/07/06/PicsArt_07-05-03.47.51.jpg
https://imgfy.net/images/2020/07/06/PicsArt_07-05-03.47.22.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-10-06-56.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-09-50-39.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-09-37-12.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-09-54-06.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-09-30-55.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-03-09-43-39.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-02-12-53-43.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-02-12-41-16.jpg
https://imgfy.net/images/2020/07/06/Pics-Art-07-02-12-49-18.jpg
https://imgfy.net/images/2020/07/03/PicsArt_06-09-05.38.52.jpg
https://imgfy.net/images/2020/07/03/1560148014021.jpg
https://imgfy.net/images/2020/07/03/Nabha-Natesh-Tits.jpg
https://imgfy.net/images/2020/07/03/NabhaNatesh6_3_5.jpg
https://imgfy.net/images/2020/07/03/nabha-natesh-ass-fucking000554.jpg
https://imgfy.net/images/2020/07/03/Nabha-Natesh-milkyilky-Boobs6a2b0f6a19f6974d.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.34.22.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.38.30.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.50.03.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.51.33.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.53.47.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.58.37.jpg
https://imgfy.net/images/2020/06/28/PicsArt_03-13-11.54.48.jpg
https://imgfy.net/images/2020/06/14/NabhaNateshKriti100594.jpg
https://imgfy.net/images/2020/06/14/Nabha-Natesh0004.jpg
https://imgfy.net/images/2020/06/14/imagesqtbn3AANd9GcQEUwBnn2TuQiv0IMeWNRjINnEVsu93IHmLCA8Ns-PC_HxmyDUlusqpCAU.jpg
https://imgfy.net/images/2020/06/14/nabha-natesh1-399x600-1.jpg
https://imgfy.net/images/2020/06/14/Nabha-Natesh-Toplesss-Posing-Boobs.jpg
https://imgfy.net/images/2020/06/14/NabhaNatesh6_3_5.jpg
https://imgfy.net/images/2020/06/14/Actress-Nabha-Natesh-Nude-Showing-Her-Boobsf75aa31f060f321f.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_nabha-natesh-nude-posing-boobs-and-pussy-jpeg.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_nabha-natesh-ass-fucking000554-md.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_actress-nabha-natesh-nude-having-sex.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_nabha-natesh-milkyilky-boobs6a2b0f6a19f6974d-md.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_nabha-natesh0003-md.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_nabha-natesh003.jpg
https://imgfy.net/images/2020/06/14/MyPornSnap.top_dimaak-kharab-nude-md.jpg
https://imgfy.net/images/2020/06/14/119227734_soq614xo-683x1024.jpg
https://imgfy.net/images/2020/06/14/119227694_9nut37x8-683x1024-1.jpg
https://imgfy.net/images/2020/06/14/119227774_8au4oqex-683x1024-1.jpg
https://imgfy.net/images/2020/06/14/119227826_8ysuxbgi-683x1024-1.jpg
https://imgfy.net/images/2020/06/14/Nabha-Natesh-Boobs-Ass-Pussy-without-dress.jpg
https://imgfy.net/images/2020/06/14/Actress-Nabha-Natesh-Nude-Showing-Her-Boobs.jpg
https://imgfy.net/images/2020/06/14/Nabha-Natesh-nude-boobs-selfie-without-clothes.jpg
https://imgfy.net/images/2020/06/14/Nabha-Natesh-Tits.jpg
https://imgfy.net/images/2020/06/14/nabha3.jpg
https://imgfy.net/images/2020/06/14/nabha1.jpg
https://imgfy.net/images/2020/06/14/nabha2.jpg"""

global nabha_list
nabha_list = nabha_data.splitlines()

