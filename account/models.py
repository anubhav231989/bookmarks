from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class FanFollowing(models.Model):

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    profile_from = models.ForeignKey("Profile", related_name="profile_from_set", on_delete=models.CASCADE)
    profile_to = models.ForeignKey("Profile", related_name="profile_to_set", on_delete=models.CASCADE)

    class Meta:
        ordering=("-created",)

    def __str__(self):
        return f"{self.profile_from} is following {self.profile_to}"
    

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
    following = models.ManyToManyField("self", related_name="followers", through=FanFollowing, symmetrical=False)

    def get_absolute_url(self):
        return reverse("profile_details", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Profile ID:{self.id} for User: {self.profile_name}"
