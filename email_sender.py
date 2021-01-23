import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


#Python 2 

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['From'] = "Gilbert Ekale"
email['To'] = "gilbertekalea@gmail.com"
email['subject'] = "Congratulations Sir!!!!!"

email.set_content(html.substitute({'name':"Gilbert"}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  #encryption
    smtp.login("gilbertekalea@gmail.com", "Amisania2010")
    smtp.send_message(email)
    print("all good boss, ready to go")

#Pyhton 3 customizing

