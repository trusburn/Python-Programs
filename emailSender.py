from email.message import EmailMessage
import ssl
import smtplib

print("=== Send Email! ===")



email_sender = input("Enter your email: ")

email_password = input("Enter App password: ")
email_reciever = input("Send to: ")

subject = input("Enter Subject: ")
body = input("""

""")



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_reciever)
    smtp.sendmail(email_sender, email_reciever, em.as_string())