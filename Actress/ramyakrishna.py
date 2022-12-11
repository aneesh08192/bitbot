from importsdata import * 

def ramyakrishna(update: Update, context: CallbackContext) -> None:
    x = ramyakrishna_list[randrange(0,len(ramyakrishna_list))]
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
        x = ramyakrishna_list[randrange(0,len(ramyakrishna_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

   # msg.delete()

ramyakrishna_data = """https://imgfy.net/images/2019/09/12/1545885837392.jpg
https://imgfy.net/images/2019/09/12/rkcopy.jpg
https://imgfy.net/images/2019/09/12/rk1copy.jpg
https://imgfy.net/images/2019/09/12/Ramya2BKrishnan3.jpg
https://imgfy.net/images/2019/09/12/ramya.png
https://imgfy.net/images/2019/09/12/RakulPreetSinghFucking.gif
https://imgfy.net/images/2019/09/12/PicsArt_08-08-12.51.05.jpg
https://imgfy.net/images/2019/09/12/1545885722005.jpg
https://imgfy.net/images/2019/09/12/1545885515610.jpg
https://imgfy.net/images/2019/09/12/154588531648719cb6571d62c339d.jpg
https://imgfy.net/images/2019/09/12/1545885316487.jpg
https://imgfy.net/images/2019/09/12/1545885196641.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nude-vagina-pussy-photos.jpg
https://imgfy.net/images/2019/09/12/ramya-krishnan-nude-pussy-fucking-fake-pictures-porn-images.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nude-milky-boobs-photos.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nude-images.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nude-getting-fucked-pics.jpg
https://imgfy.net/images/2019/09/12/ramya-krishnan-nude-fucked.png
https://imgfy.net/images/2019/09/12/ramya279kh.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nude-big-ass-photos.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nangi-images.jpg
https://imgfy.net/images/2019/09/12/ramya-krishnan-Nude-Pics.jpg
https://imgfy.net/images/2019/09/12/Ramyakrishnan-hot-saree-collection-5.jpg
https://imgfy.net/images/2019/09/12/ramyakrishna.jpg
https://imgfy.net/images/2019/09/12/Ramyakrish-dpd-copy.jpg
https://imgfy.net/images/2019/09/12/Ramya_krishna_hot_pics112-758395.jpg
https://imgfy.net/images/2019/09/12/ramyakrishnanudeboobsandnipplespressedhard.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-pressing-her-big-boobs-after-cumshot.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-oiled-big-boobs-fucked-in-cleavage-pic.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-nipple-bit-topless-big-boobs-sex-on-top.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-big-boobs-nude-in-Bathroom-Leaked.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-masturbating-with-lesbian-sex-Anushka-Shetty-xxx.jpg
https://imgfy.net/images/2019/09/12/Ramya-Krishnan-busty-boobs-naked-sexy-shaved-pussy-pic.jpg
https://imgfy.net/images/2019/09/12/ramya-krishna-nude-blue-film-photo.jpg
https://imgfy.net/images/2019/09/12/Pussy-fucking-Ramya-Krishnan-big-boobs-image.jpg
https://imgfy.net/images/2019/09/12/Nude-Baahubali-actress-Ramya-Krishnan-full-nude-sex-on-bed-1.jpg
https://imgfy.net/images/2019/09/12/Nude-ass-Ramya-Krishnan-full-nude-nipple-without-dress-1.jpg
https://imgfy.net/images/2019/09/12/New-Ramya-Krishnan-nude-pics-Hot.jpg
https://imgfy.net/images/2019/09/12/nadhiya-nude-fucked.png
https://imgfy.net/images/2019/09/12/Naked-old-actress-Ramya-Krishnan-Pussy-Fingering-Masturbating-Nude.jpg
https://imgfy.net/images/2019/09/12/Naked-fake-Ramya-Krishnan-opening-pussy-close-up-pics.jpg
https://imgfy.net/images/2019/09/12/Hot-Ramya-Krishnan-tits-nipple-photos.jpg
https://imgfy.net/images/2019/09/12/maxresdefault.jpg
https://imgfy.net/images/2019/09/12/Busty-nude-hot-Ramya-Krishnan-xxx-bikini-naked-navel-show.jpg
https://imgfy.net/images/2019/09/12/Hot-Ramya-Krishnan-showing-her-boobs-photos.jpg
https://imgfy.net/images/2019/09/12/full-nude-Ramya-Krishnan-private-sex-photo.jpg
https://imgfy.net/images/2019/09/12/f2b77cfb3ae8f1365d291dbbb48bbfb1.jpg
https://imgfy.net/images/2019/09/12/busty-fat-Ramya-Krishnan-pussy-fucking-naked-big-boobs-pressed.jpg
https://imgfy.net/images/2019/09/12/Big-fake-boobs-Ramya-Krishnan-nude-sex-pic-1.jpg
https://imgfy.net/images/2019/09/12/Big-boobs-Ramya-Krishnan-nipple-pressed-without-bra.jpg
https://imgfy.net/images/2019/09/12/Big-boobs-Ramya-Krishnan-nude-ass-photo.jpg
https://imgfy.net/images/2019/09/12/b991992542bb7dd82aa53e57ae32b541.jpg
https://imgfy.net/images/2019/09/12/Big-boobs-Ramya-Krishnan-naked-navel-pussy-pic-1.jpg
https://imgfy.net/images/2019/09/12/Big-boobs-Ramya-Krishnan-fucking-nude-sex-in-Baahubali.jpg
https://imgfy.net/images/2019/09/12/actress-ramya-krishnan-hot.jpg
https://imgfy.net/images/2019/09/12/Anushka-Shetty-pressing-Ramya-Krishnan-boobs-pussy-licked.jpg
https://imgfy.net/images/2019/09/12/Actress-Ramya-Krishnan-Nude-Sex-Naked-Without-Clothes-Nangi-Photos-13.jpg
https://imgfy.net/images/2019/09/12/881068.jpg
https://imgfy.net/images/2019/09/12/790514.jpg
https://imgfy.net/images/2019/09/12/874174.jpg
https://imgfy.net/images/2019/09/12/1RE9M.jpg
https://imgfy.net/images/2019/09/12/8e6a4789f79d9b0205763a6bdd236d14.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8815.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8824.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8805.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8825.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8784.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8823.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8811.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8798.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8799.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8803.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8808.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8782.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8775.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8787.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8800.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8785.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8813.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8819.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8780.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8804.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8801.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8788.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8773.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8796.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8802.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8814.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8822.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8786.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8778.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8817.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8774.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8795.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8776.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8791.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8792.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8781.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8777.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8797.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8816.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8789.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8783.jpg
https://img.freefake.work/images/2020/07/03/Ramya-Krishnan-Nude-South-Indian-Actress-Sex-8812.jpg"""

global ramyakrishna_list
ramyakrishna_list = ramyakrishna_data.splitlines()

