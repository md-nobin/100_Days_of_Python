from twilio.rest import Client

TWILIO_SID = "AC7e3f558a261824c99b920dfa69946cd6"
TWILIO_AUTH_TOKEN = "d5959696bfe4e65392b636284275ee35"
TWILIO_VIRTUAL_NUMBER = "+12566459794"
TWILIO_VERIFIED_NUMBER = "+8801948540317"


class NotificationManager:

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
