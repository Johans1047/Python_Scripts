import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load the environment variables
load_dotenv()

# create an object to send the headers of the mail
msg = MIMEMultipart()

# get the password (You need to config your environment variables)
password = os.getenv('PASS')

# get the absolute path
directory = os.path.dirname(os.path.abspath(__file__))

# define the template name
template_name = 'mail.html'

# Crear la ruta completa al file utilizando el directorio actual
file_path = os.path.join(directory, template_name)

def main():
    # Headers
    sender = os.getenv('USER')
    recipient = 'correodeprueba@gmail.com'
    subject = 'This is your subject'
    
    # if you want to send a bcc you can put all mails in this list
    # bbc_recipients = [ ... ] 

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    recipients = [recipient] #+ bbc_recipients

    with open(file_path,"r", encoding="utf-8") as file:
        html = file.read()
            
    # attach the html document
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    # Connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Create a secure connection
    server.starttls()
    server.login(sender, password)

    # Send the mail as a string
    server.sendmail(sender, recipients, msg.as_string())

    # Close the conexion
    server.quit()
    
if os.path.exists(file_path):
    main()
else:
    print('There is something wrong.')
