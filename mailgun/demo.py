import os
from typing import Union

import requests
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN_NAME = os.getenv("MAILGUN_DOMAIN_NAME")
MAILGUN_API_URL = (
    f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN_NAME}.mailgun.org/messages"
)


# Decorator for exception handling --------------------------------------------------------------- #
def error_handler_for_send_email(func):
    def wrapper(*args, **kwargs):
        # Init Status ------------------------------------------------------------------------------------ #
        r = None
        try:
            r = func(*args, **kwargs)
            if r.status_code == 200:
                print("Email sent successfully")
            else:
                print(f"Failed to send email. Status code: {r.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return r

    return wrapper


# Send an email using the Mailgun API ------------------------------------------------------------ #
@error_handler_for_send_email
def send_email(from_email: str, to_email: Union[str, list], subject: str, text: str):
    # Define the email parameters
    email_data = {"from": from_email, "to": to_email, "subject": subject, "text": text}

    # Send the email
    r = requests.post(
        url=MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY), data=email_data
    )

    return r


@error_handler_for_send_email
def send_email_with_attachment(
    from_email: str,
    to_email: Union[str, list],
    subject: str,
    text: str,
    attachment_paths: list,
):
    # Define the email parameters
    email_data = {"from": from_email, "to": to_email, "subject": subject, "text": text}

    # Read the attachment
    files = [
        ("attachment", open(attachment_path, "rb"))
        for attachment_path in attachment_paths
    ]

    # Send the email
    r = requests.post(
        url=MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY), data=email_data, files=files
    )

    return r


if __name__ == "__main__":
    print("Sending email...")

    send_email(
        from_email=f"Mailgun Sandbox <postmaster@{MAILGUN_DOMAIN_NAME}.mailgun.org>",
        to_email=["NAME <your.email@xxx.com>"],
        subject="Hello",
        text="This is a test email from Mailgun.",
    )

    send_email_with_attachment(
        from_email=f"Mailgun Sandbox <postmaster@{MAILGUN_DOMAIN_NAME}.mailgun.org>",
        to_email=["NAME <your.email@xxx.com>"],
        subject="Hello",
        text="This is a test email from Mailgun.",
        attachment_paths=["aws/AWS-Certified-Developer-Associate_Exam-Guide.pdf"],
    )
