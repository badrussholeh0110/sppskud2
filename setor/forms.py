from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class PetugasForm(ModelForm):
    class Meta:
        model = Petugas
        fields = '__all__'
        exclude = ['level']
        widgets = {
            'namapetugas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama petugas'}),
            'namaunit': forms.Select(attrs={'class': 'form-control'}),

        }
        lebels = {
            'nama':'Nama',
        }

class PeternakForm(ModelForm):
    class Meta:
        model = Peternak
        fields = '__all__'
        exclude = ['level']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama peternak'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alamat peternak'}),
            'namaunit': forms.Select(attrs={'class': 'form-control'}),

        }
        lebels = {
            'nama':'Nama',
        }

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        widgets = {
            'namaunit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama unit'}),
            'alamatunit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alamat unit'}),
            

        }
        lebels = {
            'nama':'Nama',
        }

class SetoranForm(ModelForm):
    class Meta:
        model = Setoran
        fields = '__all__'
        widgets = {
            'namaunit': forms.Select(attrs={'class': 'form-control'}),
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'jumlahsetoran': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.Select(attrs={'class': 'form-control'}),
            'namapetugas': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'namaunit':'Nama Unit',
            'nama':'Nama Peternak',
            'jumlahsetoran':'Jumlah Setoran',
            'harga':'Harga',
            'namapetugas':'Petugas',
        }

class HargaForm(ModelForm):
    class Meta:
        model = Harga
        fields = '__all__'
        widgets = {
            'harga': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'harga per 1 liter'}),
        }
        labels = {
            'nama':'Nama',
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Petugas'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'value': 'petugas', 'readonly': 'True'}),
        }
        labels = {
            'username': 'ID Petugas',
            'first_name': 'Nama Petugas',
            'last_name': 'Level',
        }

class UserpeternakForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID peternak'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'value': 'peternak', 'readonly': 'True'}),
        }
        labels = {
            'username': 'ID peternak',
            'first_name': 'Nama peternak',
            'last_name': 'Level',
        }