from gmail import read_and_download_attachments
from read_file_name import BoomBamm
from attachedFiltetPRO import send_threaded_reply
import time

gmail_username = "mortal369pp@gmail.com"
gmail_password = "kbze tvwu ogcf zdwk" 
search_subject = "ajaysir"
jadugar_pe_save = "/home/tspl/Documents/Script_baz_lol/jadugar"


all_massages=read_and_download_attachments(gmail_username, gmail_password, search_subject, jadugar_pe_save)
all_massages=all_massages[0]
print("Mortal Lets uplod it in dataBase only if it valid Data")
BoomBamm()
print("Mortal Uploding task Success and generated remark if you want to see remark vist productionRemark folder only have 15 seconds")
time.sleep(10)
print("10 SECOND COMPLETE")
print("Mortal Initiating Sending process")
if all_massages:
    take_it_folder = "/home/tspl/Documents/Script_baz_lol/productionRemark"
    attachment_filename= "productionMapping.csv" 
    send_threaded_reply(all_massages, gmail_username, gmail_password,take_it_folder,attachment_filename)
else:
    print(f"No email found with subject: {search_subject}")
time.sleep(10)