from django.shortcuts import render
from . import forms

def index_view(request, *args, **kwargs):
    page_title = 'Homepage'
    html_template = 'index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

def about_view(request, *args, **kwargs):
    page_title = 'About'
    html_template = 'index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)

def contact_view(request, *args, **kwargs):
    page_title = 'Contact Us'
    html_template = 'pages/contact.html'

    if request.method == 'POST':
        form = forms.contactForm(request.POST)
        if form.is_valid():
            # do_something_with_form_data(form.cleaned_data)
            return render(request, 'forms/contact_form_confirm.html')
        else:
            form = forms.contactForm()

        context = {
            'form': form,
            'page_title': page_title,
        }
        return render(request, html_template, context)
    
    else:
        form = forms.contactForm()
        html_template = 'pages/contact.html'
        page_title = 'Contact Us'

        context = {
            'form': form,
            'page_title': page_title
        }
        return render(request, html_template, context)
    
def contact_form_only(request, *args, **kwargs):
    form = forms.contactForm()
    html_template = 'forms/contact_form_only.html'

    context = {
        'form': form
    }
    return render(request, html_template, context)