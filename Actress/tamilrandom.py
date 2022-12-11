from importsdata import * 

def tamilrandom(update: Update, context: CallbackContext) -> None:
    x = tamilrandom_list[randrange(0,len(tamilrandom_list))]
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
        x = tamilrandom_list[randrange(0,len(tamilrandom_list))]
        try:
            update.message.reply_photo(str(x))
        except:
            pass
        time.sleep(int(time_space))
        
        logger.info(f"{update.message.chat_id} - {update.message.from_user} - {x}")

    #msg.delete()

tamilrandom_data = """https://imgfy.net/images/2021/10/17/received_1432669250410892.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-03-59-23-19.png
https://imgfy.net/images/2021/10/17/received_937450223659321.jpg
https://imgfy.net/images/2021/10/17/received_345115163500814-1.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-7.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-8.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-2.jpg
https://imgfy.net/images/2021/10/17/images.jpg
https://imgfy.net/images/2021/10/17/images-1.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-01-17-76.png
https://imgfy.net/images/2021/10/17/images-2.jpg
https://imgfy.net/images/2021/10/17/images-3.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-01-36-95.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-02-02-58.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-03-06-53.png
https://imgfy.net/images/2021/10/17/images-4.jpg
https://imgfy.net/images/2021/10/17/images-5.jpg
https://imgfy.net/images/2021/10/17/images-6.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-3-1.jpg
https://imgfy.net/images/2021/10/17/images-7.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-5.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-6.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-2-1.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-3-2.jpg
https://imgfy.net/images/2021/10/17/Tamil-Actress-XXX-Photos-6-683x1024.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-09-53-16.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-09-45-97.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-14-75.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-31-00.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-40-88.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-36-51.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-54-61.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-10-49-22.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-11-01-54.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-12-01-57.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-12-45-23.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-13-55-16.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-14-53-00.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-15-00-25.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-16-21-64.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-16-46-74.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-16-54-61.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-17-34-53.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-17-45-47.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-17-50-13.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-17-59-42.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-18-08-15.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-18-20-33.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-18-28-72.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-18-40-47.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-23-28-42.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-23-51-01.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-24-05-38.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-05-25-36-09.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-10-02-06.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-11-29-06.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-10-58-02.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-11-49-14.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-12-09-26.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-12-32-19.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-13-17-17.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-13-41-76.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-14-15-33.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-14-43-11.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-14-57-81.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-15-26-96.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-15-50-77.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-16-23-71.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-16-52-75.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-17-13-81.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-17-55-26.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-18-24-45.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-19-09-92.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-19-42-44.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-19-57-67.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-20-09-23.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-20-22-50.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-20-40-59.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-20-52-24.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-21-01-21.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-21-16-20.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-21-39-26.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-21-54-06.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-22-06-90.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-22-24-78.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-23-12-27.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-22-43-12.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-24-23-24.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-23-27-39.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-24-41-77.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-25-00-06.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-26-07-68.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-25-19-86.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-27-11-05.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-28-40-87.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-29-17-12.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-29-50-80.png
https://imgfy.net/images/2021/10/17/wallpapertip_tamil-movies-hd-wallpapers_596812-1.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_cleavage-wallpaper_740404.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_hot-wallpaper-indian_101419.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_ileana-d-cruz-hot_249245-1.jpg
https://imgfy.net/images/2021/10/17/216-2162535_tamil-actress-hot-wallpaper.jpg
https://imgfy.net/images/2021/10/17/216-2161886_trisha-in-black-saree.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_trisha-wallpapers_606147.jpg
https://imgfy.net/images/2021/10/17/46-464891_hot-actress-in-half-saree.jpg
https://imgfy.net/images/2021/10/17/46-464898_tamil-hot-actress-in-saree.jpg
https://imgfy.net/images/2021/10/17/11-111858_south-indian-actress-hd-wallpapers-south-indian-heroines.jpg
https://imgfy.net/images/2021/10/17/17-170137_indians-actress-hot-thighs.jpg
https://imgfy.net/images/2021/10/17/58-581349_shriya-saran-south-indian-actress-hd-wallpaper-007.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_south-indian-actress-hd_969114.png
https://imgfy.net/images/2021/10/17/218-2188484_south-indian-actress-wallpaper.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_south-indian-actress-wallpaper_2188735.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-06-52-22-12.png
https://imgfy.net/images/2021/10/17/62-625727_sneha-hd-wallpaper-south-indian-actress-sneha.jpg
https://imgfy.net/images/2021/10/17/62-625708_sneha-hd-images-wallpapers-sneha-hd.jpg
https://imgfy.net/images/2021/10/17/149-1494006_sneha-prasanna-latest-hot-hd-photos-wallpapers-6236.jpg
https://imgfy.net/images/2021/10/17/149-1497431_actress-anupama-anupama-parameswaran.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_south-indian-actress-wallpaper_2189846.jpg
https://imgfy.net/images/2021/10/17/wallpapertip_tamil-actress-wallpapers-hq_596126-1.jpg
https://imgfy.net/images/2021/10/17/43bfebf3bc0d8e810ee0579149f8a6ce.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-01-58-82.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-02-20-90.png
https://imgfy.net/images/2021/10/17/Shariya-pussy-show-3234.jpg
https://imgfy.net/images/2021/10/17/th.jpg
https://imgfy.net/images/2021/10/17/th-1.jpg
https://imgfy.net/images/2021/10/17/th-2.jpg
https://imgfy.net/images/2021/10/17/th-3.jpg
https://imgfy.net/images/2021/10/17/th-4.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-13-03-34.png
https://imgfy.net/images/2021/10/17/th-5.jpg
https://imgfy.net/images/2021/10/17/th-6.jpg
https://imgfy.net/images/2021/10/17/th-7.jpg
https://imgfy.net/images/2021/10/17/th-8.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-13-54-58.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-14-33-79.png
https://imgfy.net/images/2021/10/17/185.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-08.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-01.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-02.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-03.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-04.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-05.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-06.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-07.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-07-Z.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-10.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-27-03-67.png
https://imgfy.net/images/2021/10/17/Shruti-Ra-11.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-14.jpg
https://imgfy.net/images/2021/10/17/Shruti-Ra-15.jpg
https://imgfy.net/images/2021/10/17/1540125572958.png
https://imgfy.net/images/2021/10/17/Shruti-Ra-16.jpg
https://imgfy.net/images/2021/10/17/1540128013626.png
https://imgfy.net/images/2021/10/17/1540128177297.png
https://imgfy.net/images/2021/10/17/1540127863263.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-32-56-79.png
https://imgfy.net/images/2021/10/17/1540127389304.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-34-54-02.png
https://imgfy.net/images/2021/10/17/1545065028768.jpg
https://imgfy.net/images/2021/10/17/1545064912397.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-35-21-37.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-36-11-15.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-36-52-16.png
https://imgfy.net/images/2021/10/17/1545065676045.jpg
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-37-30-11.png
https://imgfy.net/images/2021/10/17/Screenshot_2021-10-17-07-39-36-63.png
https://imgfy.net/images/2021/10/17/1552114998116.jpg"""

global tamilrandom_list
tamilrandom_list = tamilrandom_data.splitlines()

