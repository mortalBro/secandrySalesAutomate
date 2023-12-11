import os
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header

from gmail import read_and_download_attachments

def send_threaded_reply(original_msg, smtp_username, smtp_password, save_folder,attachment_filename):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_from_email = "mortal369pp@gmail.com"

    # Extract relevant information from the original message
    sender_email = original_msg["From"]
    original_subject = original_msg["Subject"]
    original_message_id = original_msg.get("Message-ID")
    references = original_msg.get("References", "")
    in_reply_to = original_msg.get("In-Reply-To", "")

    # Create a MIMEMultipart message for the reply
    reply_subject = f"Re: {original_subject}"
    reply_body = '''Hi Team,

As per the below request we have uploaded data in production. Please verify and if you have any concern regarding the issue, please let us know.'''
    reply_msg = MIMEMultipart()
    reply_msg.attach(MIMEText(reply_body))
    reply_msg["Subject"] = reply_subject
    reply_msg["From"] = smtp_from_email
    reply_msg["To"] = sender_email
    reply_msg["References"] = f"{references} {original_message_id}" if references else original_message_id
    reply_msg["In-Reply-To"] = in_reply_to if in_reply_to else original_message_id

    # Attach a file from the save_folder
    attachment_path = os.path.join(save_folder, attachment_filename)


    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment_file:
            attachment_content = attachment_file.read()
            attachment = MIMEText(attachment_content, _subtype="plain", _charset="utf-8")
            attachment.add_header("Content-Disposition", f"attachment; filename={attachment_filename}")
            reply_msg.attach(attachment)
            print(f"Attachment added: {attachment_filename}")
    else:
        print(f"Attachment not found: {attachment_filename}")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_from_email, [sender_email], reply_msg.as_string())
        print("Threaded reply sent successfully!")
    except Exception as e:
        print(f"Error sending threaded reply: {e}")




