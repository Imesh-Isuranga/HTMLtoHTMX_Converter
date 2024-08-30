from django import forms
from .models import HTMLFile

class HTMLFileForm(forms.ModelForm):
    class Meta:
        model = HTMLFile
        fields = ['name', 'file']
        labels = {
            'name': 'File Name',
            'file': 'Upload HTML File',
        }
        help_texts = {
            'file': 'Please upload a valid HTML file.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.html'}),
        }

class HtmlConvertorForm(forms.ModelForm):
    class Meta:
        model = HTMLFile
        fields = ['name', 'file']


    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.html'):
                raise forms.ValidationError('Only HTML files are allowed.')
            if file.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError('File size must be under 2MB.')
        return file
