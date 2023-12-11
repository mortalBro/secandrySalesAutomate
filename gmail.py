import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime, timedelta  
from utility import compareDate_wrt_currentTime
import schedule
import time
# from read_file_name import BoomBamm
# from fileRafaSafa import sawakshBharat


def read_and_download_attachments(username, password, subject, save_folder="."):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    result, data = mail.search(None, f'(SUBJECT "{subject}")')
    email_ids = data[0].split()

    mortal_contain_all_message_here=[]
    for email_id in email_ids:
        result, message_data = mail.fetch(email_id, "(RFC822)")
        raw_email = message_data[0][1]

        msg = email.message_from_bytes(raw_email)
        counter=0
        if compareDate_wrt_currentTime((msg["Date"])):
            print("Wooo Conguralation Mortal Bro :",counter,"new message comes")
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")
            print(f"Subject: {subject}")
            print(f"From: {msg['From']}")
            print(f"Date: {msg['Date']}")

            for part in msg.walk():
                if part.get_content_maintype() == "multipart":
                    continue
                if part.get("Content-Disposition") is None:
                    continue

                filename = part.get_filename()

                if filename:
                    filepath = os.path.join(save_folder, filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))

                    print(f"Attachment saved: {filepath}")
                    print("Attachment saved you have only 15 sec check it in JADUGAR file there is attachment")
            mortal_contain_all_message_here.append(msg)
    mail.logout()
    return mortal_contain_all_message_here


# gmail_username = "mortal369pp@gmail.com"
# gmail_password = "enter your password"
# search_subject = "kamalsir"

# jadugar_pe_save = "/home/tspl/Documents/Script_baz_lol/jadugar"

# appolo_have_all_msg=read_and_download_attachments(gmail_username, gmail_password, search_subject, jadugar_pe_save)

# print(appolo_have_all_msg)
# for i in appolo_have_all_msg:
#     print(i.get("Message-ID"))
# print(appolo_have_all_msg.get("Message-ID"))

# def my_job():
#     message=read_and_download_attachments(gmail_username, gmail_password, search_subject, jadugar_pe_save)
#     print("Running my job MORTAL Bro")
#     time.sleep(3)
#     print("ready for bOombam")
#     BoomBamm()
#     time.sleep(10)
#     sawakshBharat()

# schedule.every(30).seconds.do(my_job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)





