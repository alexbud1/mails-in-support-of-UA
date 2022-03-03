########## libraries which are need to be installed
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##### email context
subject = "Russia is conducting environmental terrorism and crimes against humanity in Ukraine"
body = "Stop the genocide of Ukraine 🇺🇦 Russia has been conducting terror and crime against humanity on the Ukrainian land and cities for seven days already! We urge the whole international community to stop this war, because your families and homes will be next!"

##### paste your email here instead of example@gmail.com
sender_email = "example@gmail.com"

receivers = []
##### extracting emails from file and putting them into list
with open ('emails.txt', 'rt') as myfile:  
    for myline in myfile:             
        receivers.append(myline.rstrip("\n"))



##### you`ll enter your password for email in cmd/terminal
password = input("Type your password and press enter:")

##### loop for every email in list
for f in receivers:
    receiver_email = f
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email 
    message.attach(MIMEText(body, "plain"))
    ##### initialization of files to attach
    filename1 = "1.jpg"  
    filename2 = "2.jpg"  
    filename3 = "3.jpg"  
    filename4 = "4.jpg"  
    filename5 = "5.jpg"  
    filename6 = "6.jpg"  

    ##### encoding files and attaching them to message
    with open(filename1, "rb") as attachment:        
        part1 = MIMEBase("application", "octet-stream")
        part1.set_payload(attachment.read())
    encoders.encode_base64(part1)
    part1.add_header("Content-Disposition",f"attachment; filename= {filename1}",)
    message.attach(part1)

    with open(filename2, "rb") as attachment:
       
        part2 = MIMEBase("application", "octet-stream")
        part2.set_payload(attachment.read())
    encoders.encode_base64(part2)
    part2.add_header("Content-Disposition",f"attachment; filename= {filename2}",)
    message.attach(part2)

    with open(filename3, "rb") as attachment:
        
        part3 = MIMEBase("application", "octet-stream")
        part3.set_payload(attachment.read())
    encoders.encode_base64(part3)
    part3.add_header("Content-Disposition",f"attachment; filename= {filename3}",)
    message.attach(part3)

    with open(filename4, "rb") as attachment:
        
        part4 = MIMEBase("application", "octet-stream")
        part4.set_payload(attachment.read())
    encoders.encode_base64(part4)
    part4.add_header("Content-Disposition",f"attachment; filename= {filename4}",)
    message.attach(part4)

    with open(filename5, "rb") as attachment:
        
        part5 = MIMEBase("application", "octet-stream")
        part5.set_payload(attachment.read())
    encoders.encode_base64(part5)
    part5.add_header("Content-Disposition",f"attachment; filename= {filename5}",)
    message.attach(part5)

    with open(filename6, "rb") as attachment:
        
        part6 = MIMEBase("application", "octet-stream")
        part6.set_payload(attachment.read())
    encoders.encode_base64(part6)
    part6.add_header("Content-Disposition",f"attachment; filename= {filename6}",)
    message.attach(part6)

    ##### adding context to mail
    text = message.as_string()   
    context = ssl.create_default_context()

    ##### sending email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print(receiver_email + ' got mail')