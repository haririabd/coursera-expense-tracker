from django import forms

class contactForm(forms.Form):
    sender = forms.EmailField(
        label = "Email", max_length=100,
        widget=forms.EmailInput(attrs={
            "class": "hadow-sm bg-gray-50 border border-base-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light",
        }
        )
    )
    your_name = forms.CharField(
        label="Name", max_length=100,
        widget=forms.TextInput(attrs={
            "class": "shadow-sm bg-gray-50 border border-base-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light",
            }))
    message = forms.CharField(
        label = "Your message", max_length=300,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "class": "shadow-sm bg-gray-50 border border-base-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light",
        }),
        )

def clean_message(self):
    # Accept any message, unless it contains the word 'chimera'
    message = self.cleaned_data['message']
    if 'chimera' in message.lower():
        raise forms.ValidationError('What did I tell you about chimeras?!')
    return message