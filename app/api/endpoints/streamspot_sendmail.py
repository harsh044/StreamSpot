from fastapi import APIRouter,Query
from utils.response import response
from utils.dbconnect import mydb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

router = APIRouter()
mycol = mydb["streamspot"]

@router.post("/streamspot_sendmail")
def streamspot_sendmail_api(first_name,last_name,movie_name):
    sender_email = "patilharshad798@gmail.com"
    sender_password = "yvaa vcsf nocg xlbp"
    smtp_server = "smtp.gmail.com"  # e.g. "smtp.gmail.com"
    smtp_port = 587

    # Create the email content
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "patilharshad042@gmail.com"  # Recipient email
        msg['Subject'] = "New Movie Request."

        # Email body
        body = f"Name: {first_name} {last_name},\n\nMessage: {movie_name}\n\nBest regards,\n{first_name}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, "patilharshad042@gmail.com", msg.as_string())

        return response(1017)

    except Exception as e:
        return response(1005)