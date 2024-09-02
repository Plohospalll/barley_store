
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import Booking, Contact, User


class BookingForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control', 'placeholder': 'Email'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control bootstrap-datepicker'}))
    count_people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control numberpicker-input'}))
    special_request = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 5, 'class':
        'form-control', 'placeholder': 'Введите ваш комментарий...'}), max_length=500, label='comment')
    class Meta:
        model = Booking
        fields = ['username', 'email','date','count_people','special_request']

class ContactForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 2, 'class':'form-control', 'placeholder': 'Введите ваш комментарий...'}), max_length=500, label='comment')
    message = forms.Textarea(attrs={'rows': 5, 'cols': 5, 'class':'form-control',})
    class Meta:
        model = Contact
        fields = ['username', 'email','subject','message']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ваше имя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']


class CreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangeFormUser(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Имя пользователя'}),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Ваше Имя'}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Фамилия'}),required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Email'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control py-4','placeholder':'Изображение'} ),required=False)
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Номер телефона'}),required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Ваш Адрес'}),required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control py-4','placeholder':'Дата рождения'}),required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'address',
                  'telephone','date_of_birth']
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4','placeholder':'Старый пароль'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4','placeholder':'новый пароль'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Повторите новый пароль'}))
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
