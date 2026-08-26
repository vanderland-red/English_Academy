from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone, email, username, password):

        if not phone:
            raise ValueError('User must have phone number')

        if not username:
            raise ValueError('User must have username')

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            username=username
        )

        # Hash Password
        user.set_password(password)
        user.save(using=self._db)

        return user


    # Admin Panel Control
    def create_superuser(self, phone, email, username, password):
        user = self.create_user(phone, email, username, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user