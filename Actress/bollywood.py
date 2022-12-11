from importsdata import * 

def bollywood(update: Update, context: CallbackContext) -> None:
    x = bollywood_list[randrange(0,len(bollywood_list))]
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
        x = bollywood_list[randrange(0,len(bollywood_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    msg.delete()

bollywood_data = """https://imgfy.net/images/2021/04/17/fakes-xxx-Kareena-Kapoor-nude-1.jpg
https://imgfy.net/images/2021/04/17/chudai-Kareena-Kapoor-6.jpg
https://imgfy.net/images/2021/04/17/Bollywood-Actress-Kareena-Kapoor-Balwali-Choot-Chudai-Xxx-Photo-16.jpg
https://imgfy.net/images/2021/04/17/Bollywood-Actress-Kareena-Kapoor-Balwali-Choot-Chudai-Xxx-Photo-12.jpg
https://imgfy.net/images/2021/04/17/alia-srdha-9.jpg
https://imgfy.net/images/2021/04/17/Bollywood-Actress-Kareena-Kapoor-Balwali-Choot-Chudai-Xxx-Photo-3.jpg
https://imgfy.net/images/2021/04/17/alia-srdha-7.jpg
https://imgfy.net/images/2021/04/17/alia-srdha-6.jpg
https://imgfy.net/images/2021/04/17/alia-bhattxxx9.jpg
https://imgfy.net/images/2021/04/17/Alia-disha.jpg
https://imgfy.net/images/2021/04/17/alia-bhattxxx6.jpg
https://imgfy.net/images/2021/04/17/alia-bhattxxx2.jpg
https://imgfy.net/images/2021/04/17/alia-bhattxxx1.jpg
https://imgfy.net/images/2021/04/17/Alia-Bhatt-Fucked_2.png
https://imgfy.net/images/2021/04/17/Alia-Bhatt-Fucked.png
https://imgfy.net/images/2021/04/17/Alia-Bhatt-BBC-Anal.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-10_1_orig.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-16_1_orig.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-9_1_orig.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-4.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-3.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-2.jpg
https://imgfy.net/images/2021/04/17/alia-19.jpg
https://imgfy.net/images/2021/04/17/alia-17.jpg
https://imgfy.net/images/2021/04/17/alia-11.jpg
https://imgfy.net/images/2021/04/17/Alia.jpg
https://imgfy.net/images/2021/04/17/159516483_kareena-01.jpg
https://imgfy.net/images/2021/04/17/alia.fingering1.jpg
https://imgfy.net/images/2021/04/17/5120C643-32C2-431A-9E5F-392F7B293744.jpg
https://imgfy.net/images/2021/04/17/2021-03-12-5.png
https://imgfy.net/images/2021/04/17/358A9F1C-F09D-4E85-8EA8-C4435C02FE9E.jpg
https://imgfy.net/images/2021/04/17/0D46F6F8-4BF2-4A4C-BA5A-225C35EB23E5.jpg
https://imgfy.net/images/2021/04/17/22-Kareena-Kapoorcopy.jpg
https://imgfy.net/images/2021/04/17/PicsArt_09-25-03.21.48.jpg
https://imgfy.net/images/2021/04/17/PicsArt_09-19-12.56.34.jpg
https://imgfy.net/images/2021/04/17/PicsArt_09-19-12.09.13.jpg
https://imgfy.net/images/2021/04/17/PicsArt_07-21-07.05.43.jpg
https://imgfy.net/images/2021/04/17/PicsArt_07-30-01.14.51.jpg
https://imgfy.net/images/2021/04/17/PicsArt_07-18-12.07.53.jpg
https://imgfy.net/images/2021/04/17/PicsArt_06-07-11.38.13.jpg
https://imgfy.net/images/2021/04/17/PicsArt_05-27-05.03.44.jpg
https://imgfy.net/images/2021/04/17/PicsArt_05-27-05.19.45.jpg
https://imgfy.net/images/2021/04/17/Nude-Actress-Kriti-Sanon-XXX-Ass-Pussy-Fucking-Full-HD-Porn-Photos-Bollywood-Actress-Full-HD-Porn-9.jpg
https://imgfy.net/images/2021/04/17/kriti-sanon-xxx-fakes-9.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-xxx-3.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-xxx-2.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-xxx-1.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-3.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-2.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-1_2.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-Nude-1.jpg
https://imgfy.net/images/2021/04/17/Kriti-Sanon-GB.jpg
https://imgfy.net/images/2021/04/17/kriti-sanon-fk2.jpg
https://imgfy.net/images/2021/04/17/kriti-sanon-fakes-1.jpg
https://imgfy.net/images/2021/04/17/kriti-kharbanda-nude-deserved.jpg
https://imgfy.net/images/2021/04/17/kriti-kharbanda-naked.jpg
https://imgfy.net/images/2021/04/17/kriti-kharbanda-hot-photos-in-ongole-githa-hot-navel-47e155092c8f4b3207435aa53ac360ad-large-687080.jpg
https://imgfy.net/images/2021/04/17/kriti-6.jpg
https://imgfy.net/images/2021/04/17/Kriti-ass-show.jpg
https://imgfy.net/images/2021/04/17/kriti-3.jpg
https://imgfy.net/images/2021/04/17/kriti-2_2.jpg
https://imgfy.net/images/2021/04/17/kriti-2.jpg
https://imgfy.net/images/2021/04/17/kriti_sanon_nude_aishfuckers282129.jpg
https://imgfy.net/images/2021/04/17/KRITI_SANON_061.jpg
https://imgfy.net/images/2021/04/17/kriti_kharbanda7-6.jpg
https://imgfy.net/images/2021/04/17/kriti_kharbanda-6.jpg
https://imgfy.net/images/2021/04/17/Kriti_Kharbanda_PicsArt_11-04-12.19.36-01.jpg
https://imgfy.net/images/2021/04/17/kareena-nude-metoo.jpg
https://imgfy.net/images/2021/04/17/kareena-naked-03.jpg
https://imgfy.net/images/2021/04/17/kareena-ki-nangi-sex-10.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-sex-3.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-naked-11.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-naked-10.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-naked-7.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-naked-3.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-9.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-8.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor-xxx-7.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-sex-fake-10.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-sex-fake-9.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-sex-fake-6.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-porn-nude-4.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-nude-14.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-Nude-9c5ef7087758f8a1b.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-Nude-8-1.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-Nude-6.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-Nude-3-1.jpg
https://imgfy.net/images/2021/04/17/KareenaKapoorKhanAnal.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-exposing-Sexy-Boobs-Cleavage-in-Red-Hot-Saree-Kareena-Kapoor-hot-photo-starspixvix-blogspot-in-thjcopy.jpg
https://imgfy.net/images/2021/04/17/KareenaKapoorAlisex.jpg
https://imgfy.net/images/2021/04/17/Kareena-Kapoor-double-pentration.jpg
https://imgfy.net/images/2021/04/17/kareena-fuck4.jpg
https://imgfy.net/images/2021/04/17/kareena-kapoor_busty.jpg
https://imgfy.net/images/2021/04/17/Kareena-chudai-nangi-9.jpg
https://imgfy.net/images/2021/04/17/Kareena-chudai-nangi-3.jpg
https://imgfy.net/images/2021/04/17/Kareena-chudai-nangi-2.jpg
https://imgfy.net/images/2021/04/17/Kareena-3243523.jpg
https://imgfy.net/images/2021/04/17/kareena16.jpg
https://imgfy.net/images/2021/04/17/Kareena-3.jpg
https://imgfy.net/images/2021/04/17/kareena_kapoor_05.png
https://imgfy.net/images/2021/04/17/kareena2.jpg
https://imgfy.net/images/2021/04/17/Kareena-1.jpg
https://imgfy.net/images/2021/04/17/kareena_analcopy.jpg
https://imgfy.net/images/2021/04/17/kareena_fucking25-compressed.jpg
https://imgfy.net/images/2021/04/17/kareena.png
https://imgfy.net/images/2021/04/17/kareena_ajay_fuck.jpg
https://imgfy.net/images/2021/04/17/kareena.jpg
https://imgfy.net/images/2021/04/17/jePicsArt_06-28-04.20.21.jpg
https://imgfy.net/images/2021/04/17/InShot_20200227_221337528.jpg
https://imgfy.net/images/2021/04/17/InShot_20200207_194545912.jpg
https://imgfy.net/images/2021/04/17/hot-Kareena-xxx-nude-12.jpg
https://imgfy.net/images/2021/04/17/hot-Kareena-xxx-nude-10.jpg
https://imgfy.net/images/2021/04/17/hot-Kareena-xxx-nude-6.jpg
https://imgfy.net/images/2021/04/17/hot-Kareena-xxx-nude-3.jpg
https://imgfy.net/images/2021/04/17/Hot-Kareena-Kapoor-Actress.jpg
https://imgfy.net/images/2021/04/17/fuckingkareena.jpg
https://imgfy.net/images/2021/04/17/fkriti3.jpg
https://imgfy.net/images/2021/04/17/alia-bhattxxx5.jpg
https://imgfy.net/images/2021/04/17/alia-bhatt-1.jpg"""

global bollywood_list
bollywood_list = bollywood_data.splitlines()

