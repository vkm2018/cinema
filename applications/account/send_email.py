# from django.core.mail import send_mail
#
#
# def send_is_active(code,email):
#     full_link = f'http://localhost:8000/api/v1/account/active/{code}'
#     send_mail(
#         'online кинотеатр cinemakg',
#         full_link,
#         'victorkim.2016@gmail.com',
#         [email]
#     )
#
# def forgot_password_email(code, email):
#     send_mail(
#         'Восстановление пароля',
#         f'Ваш код подтверждения: {code}',
#         'victorkim.2016@gmail.com',
#         [email]
#     )
