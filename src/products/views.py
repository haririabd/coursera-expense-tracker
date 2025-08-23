from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
def add_category(request):
    form = models.AddCategoryForm()
    page_title = 'Add Category'
    html_template = 'products/add-category.html'

    if request.method == 'POST':
        form = models.AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product_categories'))
        else:
            print(form.errors.as_text)
            context = {
                'page_title': page_title,
                'form': form
            }
    else:
        context = {
            'page_title': page_title,
            'form': form
        }

        return render(request, html_template, context)

def view_categories(request):
    page_title = 'Book Categories'
    html_template = 'products/list-category.html'
    categories = models.Category.objects.all()
    n = categories.count()

    context = {
        'page_title': page_title,
        'cat': categories,
        'total': n

    }

    return render(request, html_template, context)
    

def add_book():
    pass

def view_books():
    pass