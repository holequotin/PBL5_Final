from django.forms import Form
from django import forms
from .validators import *

class UserInfoForm(Form):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'lastname',
        'placeholder' : 'Họ',
    }))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        #'class="form-control" id="inputAddress" placeholder="Nhập họ và tên" required',
        'class' : 'form-control',
        'id' : 'firstname',
        'placeholder' : 'Tên',
    }),required=True)
    #style="background-color: #ccc;" type="email" class="form-control" id="inputEmai" value="abc@gmail.com" readonly
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        # 'style' : "background-color : #ccc;",
        'type' : 'email',
        'class' : 'form-control',
        'id' : 'email',
        # 'readonly' : 'readonly'
    }), required=False)
    # address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    #     'type' : 'text',
    #     'class' : 'form-control',
    #     'id' : 'address',
    #     'placeholdr' : "Nhập địa chỉ",
    # }),required=True)
    phone_num = forms.CharField(max_length=11,widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'id' : 'phonenumber',
        'placeholder' : 'Nhập số điện thoại'
    }),required=True,validators=[validate_phone_number])