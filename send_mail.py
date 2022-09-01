# MAIL
from email.message import EmailMessage
import ssl
import smtplib
# HTML Text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_sender = "backenddeveloper.me@gmail.com"
email_receiver = "sandeepkc510@gmail.com"


email_password = "jixmzkgijnhjsygm"   #this is an email_sender generated password.
#to create email_password you have to generate/create '"App Passwords"' in Google(gmail)
# Step1 -> click 'Manage your Google Account' then click 'security'
# Step2 -> inside 'Signing in to Google' there you get 'App passwords' click that.
# or you can try this link : https://myaccount.google.com/apppasswords


subject = "Message"

s = "Sandeep"

body = f"""
<html>
<head></head>
<body>
<h4>Python Mail</h4>
<p>Hi, I am {s} from Gangtok.</p>
</body>
</html>
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
# em.set_content(body)
html = MIMEText(body, 'html')
em.set_content(html)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())