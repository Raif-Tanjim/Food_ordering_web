from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username_or_email, password, **extra_fields):
        if not username_or_email:
            raise ValueError("Username or email is required")

        email = self.normalize_email(username_or_email) if '@' in username_or_email else None
        username = username_or_email if '@' not in username_or_email else None

        if not email and not username:
            raise ValueError("Username or email is required")

        user = self.model(username=username, Email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username_or_email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username_or_email, password, **extra_fields)
