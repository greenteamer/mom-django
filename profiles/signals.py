from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(user_logged_in)
def user_logged_in_(request, user, **kwargs):
    token = Token.objects.get_or_create(user=user)
    print('>>>> token: ', token)

