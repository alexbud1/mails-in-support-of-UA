# mails-in-support-of-UA
Using this repository you can send mails to multiple recipients.Was created in support of Ukraine, to turn society`s attention to war.

# Windows

Follow instruction and do next steps.

1.Go to Google's Account Security Settings: www.google.com/settings/security

Find the field "Access for less secure apps". Set it to "Allowed".

2.You should start the Python built-in mail server on port 1025 using the following command for Windows:

      python -m smtpd -c DebuggingServer -n localhost:1025
  
3.Open another cmd window and paste command:

      python send_letters.py
  
4.You will be asked to print your email password.
Do it.
I dont save it anywhere or use(you can check it in code)

5.The process of sending started
