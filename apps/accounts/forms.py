from django import forms
from .models import User
from django.contrib.auth import authenticate
from .user_filter import validate_username, validate_phone



#================
# User Register
#================
class UserRegisterForm(forms.ModelForm):


    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'phone', 'email']

    # اعتبار سنجی کاربر
    def clean_username(self):
        username = self.cleaned_data.get('username')

        return validate_username(username)

    # اعتبار سنجی شماره تلفن کاربر
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        return validate_phone(phone)
    

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('رمزهای عبور یکسان نیستند.')

        return cleaned_data


    # Hash Password
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


#==============
# User Login
#==============
class UserLoginForm(forms.Form):

    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    # اعتبار سنجی شماره تلفن کاربر
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
    
        return validate_phone(phone)

    def clean(self):
        cleaned_data = super().clean() # گرفتن داده های معتبر

        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')

        if phone and password:
            self.user = authenticate(phone=phone, password=password)

            if self.user is None:
                raise forms.ValidationError('شماره تلفن یا رمز عبور اشتباه است.')

        return cleaned_data