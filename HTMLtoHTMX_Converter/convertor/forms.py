from django import forms


class HtmlConvertorForm(forms.Form):
            htmlInput = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your HTML code here...', 'rows': 10, 'cols': 80}),
                label='Enter HTML Code',
                required=True
            )
