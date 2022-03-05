# mails-in-support-of-UA
Using this repository you can send mails to multiple recipients.Was created in support of Ukraine, to turn society`s attention to war.

# Windows / Mac

Follow instruction and do next steps.

1.Download this repository on your device with following command:

      git clone https://github.com/alexbud1/mails-in-support-of-UA/

2.Open file in this directory called user_data.txt and find 1st and 2nd rows of code:
      
      example@gmail.com
      
      your_password
      
Paste here your email instead of example@gmail.com and password instead of your_password

3.Go to Google's Account Security Settings: www.google.com/settings/security

Find the field "Access for less secure apps". Set it to "Allowed".
  
4.Open cmd window and paste command:

      python send_letters.py

if it does not work - try this one:

      python3 send_letters.py

5.The process of sending started
