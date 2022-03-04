import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from tqdm import tqdm


##### account data for starting email sending
sender_email = "example@gmail.com"
gmail_password = 'your_password'


##### extracting emails from file and putting them into list
receivers = []
with open ('emails.txt', 'rt') as myfile:  
    for myline in myfile:     
        receivers.append(myline.rstrip("\n"))


##### data for letter
subject = "Russia is conducting environmental terrorism and crimes against humanity in Ukraine"
body = "Stop the genocide of Ukraine 🇺🇦 Russia has been conducting terror and crime against humanity on the Ukrainian land and cities for seven days already! We urge the whole international community to stop this war, because your families and homes will be next!"


##### list of files to attach to letter
filename = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg"]


##### starting SMTP server
context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls(context=context)
server.ehlo()
server.login(sender_email, gmail_password)


##### creating message object
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

##### attaching files to message
for i in range(6):  
    with open(filename[i], "rb") as attachment:        
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",f"attachment; filename= {filename[i]}",)
    message.attach(part)
    

##### sending letters to all emails in emails.txt
for f in tqdm(receivers):
    message["To"] = f   
    message["Bcc"] = f  
    text = message.as_string()  
    server.sendmail(sender_email, f, text)


server.close()
