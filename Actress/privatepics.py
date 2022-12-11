from importsdata import * 

def privatepics(update: Update, context: CallbackContext) -> None:
    x = privatepics_list[randrange(0,len(privatepics_list))]
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
        x = privatepics_list[randrange(0,len(privatepics_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

privatepics_data = """https://imgfy.net/images/2020/10/15/PicsArt_10-07-07.34.36.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-13-01.46.50.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-12-11.02.03.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-12-10.33.13.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-02-11.24.40.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-02-11.43.53.jpg
https://imgfy.net/images/2020/10/15/PicsArt_09-23-10.55.02.jpg
https://imgfy.net/images/2020/10/15/PicsArt_09-23-11.25.09.jpg
https://imgfy.net/images/2020/10/15/PicsArt_10-02-07.48.49.jpg
https://imgfy.net/images/2020/10/15/PicsArt_09-23-10.41.57.jpg
https://imgfy.net/images/2020/10/15/PicsArt_09-15-11.47.47.jpg
https://imgfy.net/images/2020/09/20/PicsArt_09-18-03.26.08.jpg
https://imgfy.net/images/2020/09/20/PicsArt_09-18-03.45.49.jpg
https://imgfy.net/images/2020/09/15/PicsArt_09-15-11.47.47.jpg
https://imgfy.net/images/2020/09/14/PicsArt_09-14-02.14.48.jpg
https://imgfy.net/images/2020/09/13/IMG_20200323_181201_325.jpg
https://imgfy.net/images/2020/09/13/IMG_20200328_111621_807.jpg
https://imgfy.net/images/2020/09/13/IMG_20200429_154126_818.jpg
https://imgfy.net/images/2020/09/13/IMG_20200429_155604_544.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-28-12.51.46.jpg
https://imgfy.net/images/2020/09/13/IMG_20200429_192943_288.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-28-02.09.32.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-28-11.02.21.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-28-10.54.44.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-28-11.27.49.png
https://imgfy.net/images/2020/09/13/PicsArt_05-28-11.22.53.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-06.53.20.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-07.10.19.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-07.34.08.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-07.50.18.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-07.19.51.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-08.19.54.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-08.30.41.jpg
https://imgfy.net/images/2020/09/13/PicsArt_05-30-08.43.42.jpg
https://imgfy.net/images/2020/09/13/PicsArt_07-28-04.32.45.jpg
https://imgfy.net/images/2020/09/13/PicsArt_06-19-12.19.40.jpg
https://imgfy.net/images/2020/09/13/PicsArt_07-28-04.21.53.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-01-08.05.50.jpg
https://imgfy.net/images/2020/09/13/PicsArt_07-28-06.08.57.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-02-12.01.40.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-02-12.20.13.jpg
https://imgfy.net/images/2020/09/13/PicsArt_07-27-08.16.23.jpg
https://imgfy.net/images/2020/09/13/PicsArt_07-28-02.58.27.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-02-12.07.59.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-06-01.00.25.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-03-01.44.23.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-06-01.24.01.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-07-05.15.06.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-07-12.12.27.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-10-01.29.49.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-12-12.24.36.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-12-03.41.05.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-12-04.03.55.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-13-12.33.12.jpg
https://imgfy.net/images/2020/09/13/IMG_20200812_184347_046.jpg
https://imgfy.net/images/2020/09/13/IMG_20200812_184353_604.jpg
https://imgfy.net/images/2020/09/13/IMG_20200812_184356_219.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-13-12.16.01.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-14-04.09.38.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-20-12.54.09.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-20-01.05.43.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-22-12.06.50.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-24-01.31.15.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-12.21.17.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-12.11.47.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-11.18.54.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-09.17.12.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-11.26.16.jpg
https://imgfy.net/images/2020/09/13/FaceApp_1598610868679.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-11.42.43.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-25-11.43.44.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-26-07.26.11.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-28-04.20.12.png
https://imgfy.net/images/2020/09/13/PicsArt_08-26-12.05.21.jpg
https://imgfy.net/images/2020/09/13/PicsArt_08-28-04.36.14.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-02.42.07.jpg
https://imgfy.net/images/2020/09/13/20200901_143121.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-03.02.06.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-03.41.38.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-10.30.03.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-09.01.32.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-01-08.34.21.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-03-02.39.25.png
https://imgfy.net/images/2020/09/13/PicsArt_09-01-10.47.21.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-03-02.52.24.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-08.59.38.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-03-08.45.18.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-03-08.50.10.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-05.45.17.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-05.54.25.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-08.39.39.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-09.09.13.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-09-11.11.13.jpg
https://imgfy.net/images/2020/09/13/PicsArt_09-04-09.18.45.jpg"""

global privatepics_list
privatepics_list = privatepics_data.splitlines()

