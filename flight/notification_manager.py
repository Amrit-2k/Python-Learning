from twilio.rest import Client
import smtplib
TWILIO_SID = "ACc23acda91e8572a066be7da918aae910"
TWILIO_AUTH_TOKEN = "a6d14ce87a8eb64a9a916a6968616046"
TWILIO_VIRTUAL_NUMBER = "+13858327824"
TWILIO_VERIFIED_NUMBER = "+64220521226"

MAIL_PROVIDER_SMTP_ADDRESS =  "smtp.gmail.com"
MY_EMAIL = ""
MY_PASSWORD = ""


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )