import os, smtplib, imghdr, getpass
from tkinter import filedialog, Tk
from email.message import EmailMessage # To Format email handle more clearly

option = input("Do you want to use default Email? (Y/N): ").lower()
if option == 'y':
    useremail = os.environ.get('useremail')
    password = os.environ.get('userpass')
else:
    useremail = input("Enter your email: ")
    password = getpass.getpass()
to = input("Receiver Email: ")# youremail@domain.com

msg = EmailMessage()
msg['Subject'] = input("Subject: ")
msg['From'] = useremail
msg['To'] = to

msg.set_content(input("Your Message: "))

option = input("Do you want to attach attachment?(Y/N): ").lower()
if option == 'y':
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file = filedialog.askopenfilename(title="Choose Attachment", filetypes=[('JPEG', '*.jpg *.jpeg'), ("PNG", "*.png"), ("BMP", "*.bmp"), ("ICON", "*.ico")])
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp: Need ehlo and starttls
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp: # This is for Email Handelling locally so ehlo, starttsl and login are disabled For CMD: py -m smtpd -c DebuggingServer -n localhost:1025
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(useremail, password)
    # subject = "This Subject" When using EmailMessage class
    # body = "Hello World!"
    # message = f"Subject: {subject}\n\n {body}"
    smtp.send_message(msg)
    # smtp.sendmail(useremail, '', message)
