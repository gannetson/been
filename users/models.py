from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    USERNAME_FIELD = 'name'


