from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "账号或手机号",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "输入您的登录密码"}))


class RegisterForm(forms.Form):

    phonenumber = forms.CharField(label="手机号", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'pattern':r'[0-9]{11}', 'oninvalid':"setCustomValidity('请输入11位手机号.')",'placeholder': "请输入您的手机号"}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "设置登录密码"}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "重复密码"}))

