from importsdata import * 

def urvashirautela(update: Update, context: CallbackContext) -> None:
    x = urvashirautela_list[randrange(0,len(urvashirautela_list))]
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
        x = urvashirautela_list[randrange(0,len(urvashirautela_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

urvashirautela_data = """https://imgfy.net/images/2021/01/12/photo6334484958512524115.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524113.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524106.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524111.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524101.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524097.jpg
https://imgfy.net/images/2021/01/12/photo6057817196962359948.jpg
https://imgfy.net/images/2021/01/12/photo6055634971323902311.jpg
https://imgfy.net/images/2021/01/12/photo6061905988648282959.jpg
https://imgfy.net/images/2021/01/12/photo6061905988648282894.jpg
https://imgfy.net/images/2021/01/12/photo6055634971323902310.jpg
https://imgfy.net/images/2021/01/12/photo6332241259007159091.jpg
https://imgfy.net/images/2021/01/12/photo6334484958512524078.jpg
https://imgfy.net/images/2020/11/28/Urvashi-rautela-2.jpg
https://imgfy.net/images/2020/11/28/Urvashi-rautela-1.jpg
https://imgfy.net/images/2020/11/28/Urvashi-rautela-3.jpg
https://imgfy.net/images/2020/11/28/Urvashi.jpg
https://imgfy.net/images/2020/10/13/121234160_667129180855125_2813246816963466119_n.jpg
https://imgfy.net/images/2020/10/13/121486693_1647777372048535_8304131359028855368_n.jpg
https://imgfy.net/images/2020/10/13/121218604_200189408141882_5600868664537523034_n.jpg
https://imgfy.net/images/2020/10/13/121231617_780775369381778_2788176630973814154_n.jpg
https://imgfy.net/images/2020/10/01/EjP4pZcUcAIFP0j.jpg
https://imgfy.net/images/2020/10/01/EjP39_gU4AwQk6g.jpg
https://imgfy.net/images/2020/10/01/EjP4qPmUcAEeaGf.jpg
https://imgfy.net/images/2020/10/01/EjP4p4eUYAAsEui.jpg
https://imgfy.net/images/2020/10/01/EjP4pnfVgAA9Ehz.jpg
https://imgfy.net/images/2020/10/01/EjP4eOlU8AEahvR.jpg
https://imgfy.net/images/2020/10/01/EjP4ehqU0AI08z0.jpg
https://imgfy.net/images/2020/10/01/EjP4d5PUcAE3afF.jpg
https://imgfy.net/images/2020/10/01/EjP4dkZUcAAfVxg.jpg
https://imgfy.net/images/2020/10/01/EjP3-m5VgAA1NkA.jpg
https://imgfy.net/images/2020/10/01/EjP3-2MU4AE7Lwr.jpg
https://imgfy.net/images/2020/10/01/EjPwhEwVgAATcPn.jpg
https://imgfy.net/images/2020/10/01/EjPw-gQU4AAwmvz.jpg
https://imgfy.net/images/2020/10/01/EjPwgyKVcAAX-5L.jpg
https://imgfy.net/images/2020/10/01/EjPwxMpVcAIN0Pi.jpg
https://imgfy.net/images/2020/10/01/EjPwWFvUYAA1zel.jpg
https://imgfy.net/images/2020/10/01/EjPww3WU8AE3wp4.jpg
https://imgfy.net/images/2020/10/01/EjPwVlhVkAArxkM.jpg
https://imgfy.net/images/2020/10/01/EjPwJxPVkAMX4T7.jpg
https://imgfy.net/images/2020/10/01/EjPwJLtVgAE1Nfd.jpg
https://imgfy.net/images/2020/10/01/EjPwJdDUYAAOC3V.jpg
https://imgfy.net/images/2020/10/01/EjPvzLAU4AIvjiw.jpg
https://imgfy.net/images/2020/10/01/EjPvy57VgAEw3Ad.jpg
https://imgfy.net/images/2020/10/01/EjPvyogVkAEgCaZ.jpg
https://imgfy.net/images/2020/10/01/EjPw_hvVgAAneI3.jpg
https://imgfy.net/images/2020/10/01/EjPw_FLUYAEYYmG.jpg
https://imgfy.net/images/2020/10/01/EjPw__aUYAA1A4A.jpg
https://imgfy.net/images/2020/10/01/EjPvicqU8AAyAeG.jpg
https://imgfy.net/images/2020/10/01/EjPviIZU8AEmiMm.jpg
https://imgfy.net/images/2020/09/17/EiHgB-yU8AA0JHM.jpg
https://imgfy.net/images/2020/09/17/EiHgBtBVgAUhsc5.jpg
https://imgfy.net/images/2020/09/17/EiHfuVTVkAECFxs.jpg
https://imgfy.net/images/2020/09/17/EiHfuq7U0AMnfUC.jpg
https://imgfy.net/images/2020/09/17/EiHfeyEU0AIzrpT.jpg
https://imgfy.net/images/2020/09/17/EiHfePrUYAEoEhf.jpg
https://imgfy.net/images/2020/09/15/Eh-PwH0VkAAqrty.jpg
https://imgfy.net/images/2020/09/15/Eh-PnT4VgAAenkY.jpg
https://imgfy.net/images/2020/09/15/Eh-Pv2iVkAASaEF.jpg
https://imgfy.net/images/2020/09/15/Eh-PnBgU8AAzxOM.jpg
https://imgfy.net/images/2020/09/15/Eh-PfNVUwAA29Y.jpg
https://imgfy.net/images/2020/09/15/Eh-Pe8RUcAAV1GJ.jpg
https://imgfy.net/images/2020/09/15/Eh-P0xJUMAAHd4h.jpg
https://imgfy.net/images/2020/09/15/Eh-P3ttU4AAvJel.jpg
https://imgfy.net/images/2020/07/09/IMG_20200708_015513_858a.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-05.09.59.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-05.32.15.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-05.23.44.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-04.59.05.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-22-11.38.10.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-22-11.31.20.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-22-11.03.42.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-22-10.50.40.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-21-02.00.19.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-21-02.02.25.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-12.14.41.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-12.02.39.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-04.22.15.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-23-04.19.47.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-20-10.09.54.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-21-01.42.37.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-15-12.58.43.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-15-11.00.07.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-15-10.52.10.jpg
https://imgfy.net/images/2020/04/23/PicsArt_04-15-10.00.20.jpg
https://imgfy.net/images/2020/04/02/PicsArt_12-24-03.21.04.jpg
https://imgfy.net/images/2020/04/02/PicsArt_04-01-12.17.38.jpg
https://imgfy.net/images/2020/04/02/PicsArt_04-01-12.10.48.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-10.55.06.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-10.54.18.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.48.339e1c6d7a7da21cee.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.47.43b4f71d19beaba1ef.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-09.18.56dfc449b5eac6d7b7.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-08.25.22.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-08.23.16.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-08.23.13.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-03.44.19.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-03.09.26.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-03.42.45.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-03.22.46.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-02.51.59.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-02.38.24.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-02.37.34.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-10.53.49.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-31-08.45.00.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-31-08.44.07.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-30-12.37.51.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.48.33.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.47.43.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.24.56.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-29-09.20.40.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-09.18.56.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-01.51.16.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-23-01.52.47.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-25-09.18.51.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-19-11.50.30.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-19-10.43.07.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-19-10.21.15.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-11.21.18.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-11.14.02.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-11.10.35.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-10.42.19.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-17-10.35.22.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-18-03.41.15.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-09-08.27.41.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-09-08.25.11.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-05-03.28.41.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-05-03.17.37.jpg
https://imgfy.net/images/2020/04/02/PicsArt_03-02-04.32.05.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-20-06.14.05.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-13-06.33.18.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-13-06.41.58.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-13-05.50.26.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-13-05.16.43.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-13-05.38.02.jpg
https://imgfy.net/images/2020/04/02/PicsArt_02-07-10.16.28.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-26-04.53.14.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-26-04.55.14.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-14-11.21.23.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-14-10.52.23.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-18-11.41.57.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-15-07.32.16.jpg
https://imgfy.net/images/2020/04/02/PicsArt_01-01-08.44.21.jpg
https://imgfy.net/images/2020/01/16/urvashi-61.jpg
https://imgfy.net/images/2020/01/16/urvashi-58.jpg
https://imgfy.net/images/2020/01/16/urvashi-52.jpg
https://imgfy.net/images/2020/01/16/urvashi-55.jpg
https://imgfy.net/images/2020/01/16/urvashi-48.jpg
https://imgfy.net/images/2020/01/16/urvashi-45.jpg
https://imgfy.net/images/2020/01/16/urvashi-41.jpg
https://imgfy.net/images/2020/01/16/urvashi-39.jpg
https://imgfy.net/images/2020/01/16/urvashi-34.jpg
https://imgfy.net/images/2020/01/16/urvashi-33.jpg
https://imgfy.net/images/2020/01/16/urvashi-31.jpg
https://imgfy.net/images/2020/01/16/urvashi-25.jpg
https://imgfy.net/images/2020/01/16/urvashi-22.jpg
https://imgfy.net/images/2020/01/16/urvashi-21.jpg
https://imgfy.net/images/2020/01/16/urvashi-15.jpg
https://imgfy.net/images/2020/01/16/urvashi-10.jpg
https://imgfy.net/images/2020/01/16/urvashi-6.jpg
https://imgfy.net/images/2020/01/16/urvashi-4.jpg
https://imgfy.net/images/2020/01/16/urvashi-3.jpg
https://imgfy.net/images/2020/01/16/urvashi-2.jpg
https://imgfy.net/images/2020/01/16/urvashi-1.jpg
https://imgfy.net/images/2019/10/14/tumblr_4a985c802abf38bebe567212109bd844_dbfdee36_640.jpg
https://imgfy.net/images/2019/09/10/IMG_20181210_030647_168.jpg
https://imgfy.net/images/2018/07/16/DiNzh5XXUAE6FEg.jpg
https://imgfy.net/images/2018/07/16/bf.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_31761306_370065783494663_5582308817271521280_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_31557055_185517678767993_1915552931524902912_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30590439_164865364211144_8987277508499996672_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30604415_764763463719969_266303769241714688_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_32070153_785515298309577_6443830410186063872_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_31326363_1650974978285125_7613875326631804928_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_31117210_395628630901813_8823265725511630848_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30603209_580776178974931_3449201086236196864_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30855911_1715014378591801_7734369092227825664_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30590292_161195261238070_6177405342477975552_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30087671_306081589924412_5762307636766703616_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30084245_376678206144980_5197957597021339648_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_29740021_417839762000963_3195986908433874944_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_29715053_866128513566400_1955746927697985536_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_30076682_618882085127207_182429672200470528_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_29088618_587916388231099_4071821295178743808_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28764435_232878703924834_3589185817148391424_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28751726_373249386488706_3850126593871577088_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_29403354_224023848342359_6143432670857658368_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28766675_412676749167401_3583870387097698304_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28433349_179626922674066_6737530766491648000_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28433148_1999080610307332_794256551018758144_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28154597_150218038992703_2882743484563849216_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28152882_635586906799779_70269839670771712_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_28152782_1706068579473814_6696339642121191424_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_27878746_1907639932815945_687246749349183488_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_27579432_771521746390143_5029643519522766848_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26872691_1979483888981230_4594145797192286208_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26871797_143980083063861_9177979717209292800_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26871108_2031639187112500_15894089119563776_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26434433_703021859904735_5386955592772354048_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26401802_935787996582947_2266612086442295296_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26384169_974567649365348_3266277604465836032_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26310335_2143156665908180_85970114096136192_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26286088_965380873626790_772608064716013568_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26267169_1878292612241994_3345114958999322624_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26154686_1681791291905630_8568279096310628352_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26070971_186787302068518_6352532548073029632_n.jpg
https://imgfy.net/images/2018/05/14/editing.kingsss1_26071527_1550820145010333_6521963866824376320_n.jpg"""

global urvashirautela_list
urvashirautela_list = urvashirautela_data.splitlines()

