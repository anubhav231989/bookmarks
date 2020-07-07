from django.urls import path
from .views import create_image, image_details, do_action_on_image, listing

app_name = "images"
urlpatterns = [
    path("", listing, name="listing"),
    path("create/", create_image, name="create"),
    path("details/<int:pk>/", image_details, name="details"),
    path("like/", do_action_on_image, name="image_action"),
]