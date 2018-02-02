from django import forms

class MultiPhotoForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Image Files')

    def save(self):
        return self
