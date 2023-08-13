from django import forms
from django.forms import ModelForm
from apps.models import *


class FormHero(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormHero, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['image'].label = 'Gambar'
        self.fields['title'].label = 'Judul'

    class Meta:
        model = Hero
        fields = '__all__'

        widgets = {
            'image': forms.FileInput({'class': 'form-control'}),
            'title': forms.TextInput({'class': 'form-control'}),
        }


class FormMember(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormMember, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['name'].label = 'Nama Lengkap'
        self.fields['phone'].label = 'Nomor Telepon'
        self.fields['ig'].label = 'Instagram'
        self.fields['ig'].required = False
        self.fields['status'].label = 'Status'
        self.fields['target'].label = 'Target Pembelian'

    class Meta:
        model = Members
        fields = '__all__'

        choices = [
            ('', 'Pilih Status'),
            ('Distributor', 'Distibutor'),
            ('Agen', 'Agen'),
            ('Reseller', 'Reseller'),
            ('Marketer', 'Marketer'),
        ]

        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'phone': forms.TextInput({'class': 'form-control', 'type': 'tel', 'placeholder': '08xxxxxxxxxx'}),
            'ig': forms.TextInput({'class': 'form-control'}),
            'status': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'target': forms.TextInput({'class': 'form-control'}),
        }
