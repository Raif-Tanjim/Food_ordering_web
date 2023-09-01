from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model



class UserManager(BaseUserManager):
    def create_user(self, Number,password, **extra_fields):
        if not Number:
            raise ValueError("Phone number is required")
        
        extra_fields["email"] = self.normalize_email(extra_fields.get("email"))
        user = self.model(Number=Number, **extra_fields)
        user.set_password(password)
        user.save(using =self.db)
        return user
        
    def create_superuser(self, Number,password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(Number,password, **extra_fields)