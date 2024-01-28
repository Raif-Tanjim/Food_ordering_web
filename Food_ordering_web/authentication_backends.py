from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class CustomUserAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if '@' in username:
                user = User.objects.get(Email=username)
            else:
                user = User.objects.get(username=username)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
