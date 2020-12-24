import smtplib

# Information of the sender and reciever
sender = 'your.emailid@gmail.com'
sender_pass = 'YourE-mailP@ssword'
reciever = str(input('Enter the email id of the person you want to send the mail:\n>'))

# Subject & Message of the Mail
subject = str(input("What's the subject for the mail:\n>"))
msg = str(input(("Enter you Message:\n>")))

# Mail Process
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(sender, sender_pass)
header = 'To: ' + reciever + '\n' + 'From: ' + sender + '\n' + 'Subject: ' + subject + '\n'
content = header + msg
mail.sendmail(sender, reciever, content)
mail.close()

# Notification when mail has been send!!
print('Your Mail has been send!')