from importsdata import * 

def anupama(update: Update, context: CallbackContext) -> None:
    x = anupama_list[randrange(0,len(anupama_list))]
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
        x = anupama_list[randrange(0,len(anupama_list))]
        try:
           update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

anupama_data = """https://imgfy.net/images/2020/07/06/Anupama-6.jpg
https://imgfy.net/images/2020/07/06/Anupama-5.jpg
https://imgfy.net/images/2020/07/06/Anupama-4.jpg
https://imgfy.net/images/2020/07/06/Anupama-3.jpg
https://imgfy.net/images/2020/07/06/Anupama-1.jpg
https://imgfy.net/images/2020/07/06/Anupama-2.jpg
https://imgfy.net/images/2020/07/06/Anupama1120.jpg
https://imgfy.net/images/2020/07/06/6d2c1280ed6a082e9.jpg
https://imgfy.net/images/2020/07/06/52c5ece9fab0e01d5.jpg
https://imgfy.net/images/2020/07/06/4d691181f7f14b43c.jpg
https://imgfy.net/images/2020/07/06/34406071e4eee5b60.jpg
https://imgfy.net/images/2020/07/06/1be2228fb65defb53.jpg
https://imgfy.net/images/2020/07/06/2174e9c38297c241d.jpg
https://imgfy.net/images/2020/07/06/412a38554f406f5e8.jpg
https://imgfy.net/images/2020/07/06/34786328f72af1b0a.jpg
https://imgfy.net/images/2020/07/06/2a5260a4bbd902bf4.jpg
https://imgfy.net/images/2020/07/06/1234e4f76932a1c22.jpg
https://imgfy.net/images/2020/06/28/20190425181816.jpg
https://imgfy.net/images/2020/06/28/20190428090207.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-17-05.29.11-01-01e05927f2f7dbb3c2.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_02-03-12.19.20-012af08d5eae1fca35.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_02-03-05.12.30-0189b6726d23611463.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-17-10.58.04-01dbca373fc42bbdf2.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-17-10.32.29-01a1dc0928188e2f11.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-16-12.18.12-01058158b0f1c75aaf.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-17-01.54.45-01cc28dbf3b64e17d7.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-15-11.49.04-01a3631ec11cf8be19.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-15-12.26.00-0153b25ad5e9d369d7.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-14-08.55.42-01a1d1100a55169d50.jpg
https://imgfy.net/images/2020/06/28/Anupama_Parameswaran_PicsArt_03-15-10.50.00-01171eff72c72139af.jpg
https://imgfy.net/images/2020/06/28/fpqyv949ewov.jpg
https://imgfy.net/images/2020/06/28/image.png
https://imgfy.net/images/2020/06/28/Anupama-2.jpg
https://imgfy.net/images/2020/06/28/Anupama-4.jpg
https://imgfy.net/images/2020/06/28/Anupama-3.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-25-06-48-09.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-05-43-10.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-05-46-58.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-05-27-21.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-04-50-14.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-04-41-56.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-03-56-31.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-03-02-37.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-03-12-24.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-24-03-46-07.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-14-01-33-57.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-14-01-26-41.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-14-01-56-51.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-14-01-17-55.jpg
https://imgfy.net/images/2020/06/28/IMG-20200303-162012-067.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-03-04-13-06.png
https://imgfy.net/images/2020/06/28/Pics-Art-03-04-08-10-36.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-04-08-20-53.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-05-10-34-55.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-06-10-53-28.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-03-06-11-43-53.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-02-29-05-35-12.png
https://imgfy.net/images/2020/06/28/Pics-Art-02-29-05-42-25.png
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-07-23-45.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-07-18-27.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-07-12-35.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-07-08-05.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-49-04.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-42-09.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-34-42.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-28-27.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-11-38.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-06-20-16.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-16-05-59-33.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-15-08-08-42.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-15-08-12-03.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-01-01-50-44.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-01-02-01-52.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-01-01-34-31.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-06-01-01-22-41.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-03-54-07.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-12-37-15.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-12-25-14.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-12-12-22.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-12-07-23.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-30-02-54-46.jpg
https://imgfy.net/images/2020/06/28/Pics-Art-05-31-12-00-01.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6470.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6468.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6461.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6465.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6469.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6474.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6473.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6492.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6476.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6467.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6453.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6482.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6451.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6486.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6477.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6471.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6490.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6493.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6466.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6463.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6475.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6495.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6488.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6460.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6484.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6494.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6457.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6452.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6462.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6478.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6489.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6464.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6487.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6454.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6479.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6485.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6481.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6472.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6480.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6491.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6456.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6459.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6458.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6455.jpg
https://img.freefake.work/images/2020/07/03/Anupama-Parameswaran-Nude-South-Indian-Actress-Sex-6483.jpg
https://imgfy.net/images/2021/02/24/zwP3TW.jpg
https://imgfy.net/images/2021/02/24/zwODz7.jpg
https://imgfy.net/images/2021/02/24/zwiypj.jpg
https://imgfy.net/images/2021/02/24/zwipfq.jpg
https://imgfy.net/images/2021/02/24/zJnYdj.jpg
https://imgfy.net/images/2021/02/24/zwiblE.jpg
https://imgfy.net/images/2021/02/24/zJnWhU.jpg
https://imgfy.net/images/2021/02/24/zJn13E.jpg
https://imgfy.net/images/2021/02/24/zJjjKI.jpg
https://imgfy.net/images/2021/02/24/zJuW9J.jpg
https://imgfy.net/images/2021/02/24/zJumSK.jpg
https://imgfy.net/images/2021/02/24/zJuSY7.png
https://imgfy.net/images/2021/02/24/zJubRI.png
https://imgfy.net/images/2021/02/24/zJuEV9.png
https://imgfy.net/images/2021/02/24/zJuC95.png
https://imgfy.net/images/2021/02/24/zJuaSk.png
https://imgfy.net/images/2021/02/24/zJu4no.png
https://imgfy.net/images/2021/02/24/zJuP2r.png
https://imgfy.net/images/2021/02/24/zJuVtb.png
https://imgfy.net/images/2021/02/24/zJuqF0.png
https://imgfy.net/images/2021/02/24/zJA1Wt.jpg
https://imgfy.net/images/2021/02/24/zJuXZD.png
https://imgfy.net/images/2021/02/24/zJKOf9ee382543e5b16410.jpg
https://imgfy.net/images/2021/02/24/zJFhu0765669eacc1384a8.jpg
https://imgfy.net/images/2021/02/24/zJ1Ofq.jpg
https://imgfy.net/images/2021/02/24/zJHxS0.jpg
https://imgfy.net/images/2021/02/24/zJ1tlE.jpg
https://imgfy.net/images/2021/02/24/zJvkJG.jpg
https://imgfy.net/images/2021/02/24/zJvtxK.jpg
https://imgfy.net/images/2021/02/24/zJvxbs.jpg
https://imgfy.net/images/2021/02/24/zJv0oJ.jpg
https://imgfy.net/images/2021/02/24/zJvTat.jpg
https://imgfy.net/images/2021/02/24/zJvivE.jpg
https://imgfy.net/images/2021/02/24/zwNxbj.jpg
https://imgfy.net/images/2021/02/24/zwQWUe.jpg
https://imgfy.net/images/2021/02/24/zwt4Va.jpg
https://imgfy.net/images/2021/02/24/zwN0Ha.jpg
https://imgfy.net/images/2021/02/24/zwNTae1.jpg
https://imgfy.net/images/2021/02/24/zwt5eQ.jpg
https://imgfy.net/images/2021/02/24/zw3M05.png
https://imgfy.net/images/2021/02/24/zw3Rc9.png
https://imgfy.net/images/2021/02/24/zw3vH7.png
https://imgfy.net/images/2021/02/24/zwTBS9.jpg
https://imgfy.net/images/2021/02/24/zwTLYW.jpg
https://imgfy.net/images/2021/02/24/zwTvIL.jpg
https://imgfy.net/images/2021/02/24/FEtjADlj_o.jpg
https://imgfy.net/images/2021/02/24/zJpvXW.jpg
https://imgfy.net/images/2021/02/24/zJK11a.jpg
https://imgfy.net/images/2021/02/24/zJK5pG.jpg
https://imgfy.net/images/2021/02/24/zJKWGQ.jpg
https://imgfy.net/images/2021/02/24/zJKvjI.jpg
https://imgfy.net/images/2021/02/24/zJmUTK.jpg
https://imgfy.net/images/2021/02/24/zJKese.jpg
https://imgfy.net/images/2021/02/24/zJK7fR.jpg
https://imgfy.net/images/2021/02/24/zJKjkp.jpg
https://imgfy.net/images/2021/02/24/zJKoA6.jpg
https://imgfy.net/images/2021/02/24/zJydQO.jpg
https://imgfy.net/images/2021/02/24/zJDAZe.jpg
https://imgfy.net/images/2021/02/24/zJD6Rb.jpg
https://imgfy.net/images/2021/02/24/zJK4qO.jpg
https://imgfy.net/images/2021/02/24/zJFQoI.jpg
https://imgfy.net/images/2021/02/24/zJFcaD.jpg
https://imgfy.net/images/2021/02/24/zJFyvr.jpg
https://imgfy.net/images/2021/02/24/zJFhu0.jpg
https://imgfy.net/images/2021/02/24/zJFr0J.jpg
https://imgfy.net/images/2021/02/24/zJF2ch.jpg
https://imgfy.net/images/2021/02/24/zJKZ3o.jpg
https://imgfy.net/images/2021/02/24/zJKz3q.jpg
https://imgfy.net/images/2021/02/24/zJKsBk.jpg
https://imgfy.net/images/2021/02/24/zJKOf9.jpg
https://imgfy.net/images/2021/02/24/zJKih5.jpg"""

global anupama_list
anupama_list = anupama_data.splitlines()

