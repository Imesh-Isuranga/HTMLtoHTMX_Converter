from django.shortcuts import render
from convertor.forms import HtmlConvertorForm

def Convertor(request):
    if request.method == 'POST':
        form = HtmlConvertorForm(request.POST)
        if form.is_valid():
            htmlInput = form.cleaned_data['htmlInput']
            if request.headers.get('Hx-Request'):  # Check if the request is an HTMX request
                return render(request, 'converted_htmx.html', {'htmlInput': htmlInput})
            return render(request, 'convertor.html', {'form': form, 'htmlInput': htmlInput})
    else:
        form = HtmlConvertorForm()

    return render(request, 'convertor.html', {'form': form})

