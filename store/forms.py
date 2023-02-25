from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        widgets = {
            'cid': forms.TextInput(attrs={'class': 'form-control', 'size': 15, 'maxlength': 13}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'size': 13, 'maxlength': 10}),

        }
        labels = {
            'cid': 'รหัสประจำตัว (User Name)',
            'name': 'ชื่อลูกค้า',
            'address': 'ที่อยู่',
            'tel': 'เบอร์โทรศัพท์',
        }

    def updateForm(self):
        self.fields['cid'].widget.attrs['readonly'] = True
        self.fields['cid'].label = 'รหัสประจำตัว (User Name) [ไม่อนุญาตให้แก้ไขได้]'


class ChangePasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    oldPassword = forms.CharField(label='รหัสผ่านเดิม', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่', max_length=100,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ResetPasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่', max_length=100,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
