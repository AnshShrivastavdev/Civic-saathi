import smtplib
from email.message import EmailMessage
import os

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(department_email, complaint, category="General"):
    if not EMAIL or not PASSWORD:
        raise Exception("EMAIL_ADDRESS or EMAIL_PASSWORD environment variables are not set.")

    if not department_email:
        raise Exception("No department email address provided.")

    msg = EmailMessage()
    msg['Subject'] = f"New Civic Complaint – {category} Department"
    msg['From'] = EMAIL
    msg['To'] = department_email
    msg.set_content(f"""
New Complaint Received
======================
Department : {category}
Forwarded To: {department_email}

Complaint:
{complaint}

-- 
This is an automated message from the Civic Complaint System.
""")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        raise Exception(
            "Gmail authentication failed. Make sure you're using an App Password, "
            "not your regular Gmail password. "
            "Generate one at: https://myaccount.google.com/apppasswords"
        )
    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send email: {str(e)}")
