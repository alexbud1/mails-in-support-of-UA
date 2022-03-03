# mails-in-support-of-UA
Using this repository you can send mails to multiple recipients.Was created in support of Ukraine, to turn society`s attention to war.

# Windows / Mac

Follow instruction and do next steps.

1.Download this repository on your device with following command:
      git clone https://github.com/alexbud1/mails-in-support-of-UA/

2.Go to Google's Account Security Settings: www.google.com/settings/security

Find the field "Access for less secure apps". Set it to "Allowed".

3.You should start the Python built-in mail server on port 1025 using the following command for Windows:

      python -m smtpd -c DebuggingServer -n localhost:1025
      
if it does not work - try this one:

      python3 -m smtpd -c DebuggingServer -n localhost:1025
  
4.Open another cmd window and paste command:

      python send_letters.py

if it does not work - try this one:

      python3 send_letters.py
      
5.You will be asked to print your email password.
Do it.
I dont save it anywhere or use(you can check it in code)

6.The process of sending started
