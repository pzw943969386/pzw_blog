from django import forms
from django.contrib.auth.models import User
from user.models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20,min_length=6,required=True)
    password = forms.CharField(max_length=20,min_length=8,required=True)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        max_length=32,
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '输入密码'}),
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码不能大于32位',
            'min_length': '密码不能小于6位',
        }
    )
    r_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}),
        error_messages={
            'required': '确认密码不能为空',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email','password','r_password')
        labels = {
            'username':'用户名',
            'email':'邮箱',
        }

        widgets = {
            'username':forms.widgets.TextInput(attrs={'class':'form-control','autocomplete':'off','placeholder': '用户名'}),
            'email':forms.widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': '输入邮箱地址'}),
        }


    def clean_username(self):
        username = self.cleaned_data.get('username')
        ret = User.objects.filter(username=username).exists()
        if ret:
            raise ValidationError('该用户名已经存在')
        else:
            return username

    def clean_email(self):
        email_value = self.cleaned_data.get('email')
        is_exist = User.objects.filter(email=email_value)
        if is_exist:
            raise ValidationError('邮箱已被注册')
        else:
            return email_value


    def clean(self):
        data = self.cleaned_data
        if data.get('password') == data.get('r_password'):
            return data
        else:
            self.add_error('r_password',"密码输入不一致,请重试。")
            raise ValidationError('密码输入不一致')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('img','phone', 'describe')
