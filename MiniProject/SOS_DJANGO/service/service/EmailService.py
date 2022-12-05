from django.core.mail import EmailMessage

from service.service.EmailBuilder import EmailBuilder


class EmailService:
    @staticmethod
    def send(msg, sendingMail, user ):
        if (sendingMail == "signUp"):
            text = EmailBuilder.sign_up(user)
            email = EmailMessage(msg.subject, text, msg.frm, msg.to)
            email.content_subtype = 'html'

            try:
                res = email.send()
            except Exception as e:
                res = e
        if (sendingMail == "ForgetPassword"):
            text = EmailBuilder.forgot_password(user)
            email = EmailMessage(msg.subject, text, msg.frm, msg.to)
            email.content_subtype = 'html'

            try:
                res = email.send()
            except Exception as e:
                res = e

        return res
