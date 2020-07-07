from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="images_bookmarked", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(get_user_model(), related_name="images_liked", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("images:details", kwargs={"pk": self.id})
    

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

