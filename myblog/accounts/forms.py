from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import CustomUser
from django_recaptcha.fields import ReCaptchaField
from .utils import validate_email_domain

class CustomUserCreationForm(UserCreationForm):
    """
    회원가입 폼
    """
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email')
    captcha = ReCaptchaField()  # ReCaptchaField 추가

    class Meta:
        model = CustomUser
        fields = ("last_name", "first_name", "username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # 이메일 도메인 유효성 검사 호출
        validate_email_domain(email)
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """
    사용자 정보 업데이트 폼
    """
    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'email', 'profile_picture', 'bio']


class CustomPasswordChangeForm(SetPasswordForm):
    """
    비밀번호 변경 폼
    """
    pass
