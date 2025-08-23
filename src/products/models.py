from django.db import models
from django import forms

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.category)
    
    class Meta:
        verbose_name_plural = "categories"

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        widgets = {
           'category': forms.TextInput(attrs={
               'class': "shadow-sm bg-gray-50 border border-base-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light"
           })
        }

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    productid = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.category) + ' - ' + self.title
