from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib import request

class CreateImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ("title", "url", "description")
        widgets = {
            "url": forms.HiddenInput
        }

    '''
    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_image_extensions = ["jpg", "jpeg"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_image_extensions:
            raise forms.ValidationError("The provided image url does not have valid image extension. Only jpg and jpeg formats are allowed.")

        return url
    '''

    def save(self, commit=True):
        image = super().save(commit=False)
        url = self.cleaned_data["url"]
        # extension = url.rsplit(".", 1)[1].lower()
        extension = "jpeg"
        name = slugify(image.title)
        image_name = f"{name}.{extension}"
        downloaded_image = request.urlopen(url)
        image.image.save(image_name, ContentFile(downloaded_image.read()), save=False)

        if commit:
            image.save()

        return image

        

