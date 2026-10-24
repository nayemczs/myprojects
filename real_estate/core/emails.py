from flask_mail import Mail, Message
from settings.settings import MAIL_DEFAULT_SENDER, MAIL_GUN_URL, MAIL_GUN_API_KEY, MAIL_DEFAULT_SERVICE
import requests

mail = Mail()


class EmailServices:

    @classmethod
    def get_default_service(cls):
        if MAIL_DEFAULT_SERVICE == 'mail_gun_api':
            return MailGunService()
        else:
            return EmailService()


class EmailService:
    service_app = mail
    message = None

    def set_message(self, subject, text_content, html_content, recipients, sender=None, reply_to=None):
        self.message = Message(
            sender=sender,
            recipients=[recipients],
            subject=subject,
            body=text_content,
            html=html_content,
            reply_to=reply_to
        )

    def send(self):
        self.service_app.send(self.message)
        return True


class MailGunService:
    sender = MAIL_DEFAULT_SENDER
    service_app = mail
    message = None
    url = MAIL_GUN_URL
    auth = ('api', MAIL_GUN_API_KEY)

    def set_message(self, subject, text_content, html_content, recipients, sender=None, reply_to=None):
        if sender is not None:
            self.sender = sender

        self.message = {
            'from': self.sender,
            'to': recipients,
            'subject': subject,
            'text': text_content,
            'html': html_content
        }

        if reply_to is not None:
            self.message['h:Reply-To'] = reply_to

    def send(self):
        response = requests.post(
            self.url,
            auth=self.auth,
            data=self.message
        )
        print(response.text)
        if response.status_code == 200:
            return True
        return False
