from django import forms

# برای تمیزی اینجا قسمت های مربوط به نام کاربری و شماره موبایل فیلتراش نوشتیم

def validate_username(username):

    if username and len(username) < 5:
        raise forms.ValidationError(
            'نام کاربری نمی‌تواند کمتر از ۵ کلمه باشد.'
        )

    return username


def validate_phone(phone):

    if phone:

        if not phone.isdigit():
            raise forms.ValidationError(
                'شماره موبایل باید فقط شامل عدد باشد.'
            )

        if len(phone) != 11:
            raise forms.ValidationError(
                'شماره موبایل باید دقیقاً ۱۱ رقم باشد.'
            )

        if not phone.startswith('09'):
            raise forms.ValidationError(
                'شماره موبایل باید با 09 شروع شود.'
            )

    return phone