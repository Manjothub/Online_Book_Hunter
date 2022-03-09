from django.core.mail import send_mail
from django.conf import settings
def student_verification_token(useremail,token):

                msg=f"click this link to verify your account http://127.0.0.1:8000/verify-email/{token}"
                try:
                    send_mail(
                        'Verify Email',
                        msg,
                        settings.EMAIL_HOST_USER,
                        [useremail,]
                    )
                except Exception as e:
                    print(e)
             