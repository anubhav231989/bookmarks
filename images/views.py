from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import Image
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from actions.utils import register_action

@login_required
def create_image(request):
    if request.method == "POST":
        create_image_form = CreateImageForm(request.POST)
        if create_image_form.is_valid():
            image = create_image_form.save(commit=False)
            image.user = request.user
            image.save()
            # REGISTERING ACTION TO BE USED IN ACTIVITY FEED.
            register_action(request.user, "bookmarked image", image)
            messages.success(request, "Image added successfully.")

            # REDIRECT TO IMAGE DETAIL VIEW.
            return redirect(image.get_absolute_url())
    else:
        create_image_form = CreateImageForm(data = request.GET)
        return render(request, "images/create_image.html", {"section": "images", "create_image_form": create_image_form})

# TRY TO IMPLEMENT THIS AS CLASS BASED VIEW.
@login_required
def image_details(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, "images/details.html", {"section": "images", "image": image})

@ajax_required
@login_required
@require_POST
def do_action_on_image(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
                # REGISTERING ACTION TO BE USED IN ACTIVITY FEED.
                register_action(request.user, "liked", image)
            elif action == "unlike":
                image.users_like.remove(request.user)

            # CAN RETURN THE IMAGE DATA ALONG WOTH STATUS OF THE REQUEST.
            return JsonResponse({"status": "SUCCESS"})
        except:
            pass
            
    return JsonResponse({"status": "ERROR"})

@login_required
def listing(request):
    images = Image.objects.all()
    images_paginator = Paginator(images, 8)
    page = request.GET.get("page")
    try:
        images = images_paginator.page(page)
    except PageNotAnInteger:
        images = images_paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse("")

        images = images_paginator.page(images_paginator.num_pages)
    context = {"section": "images", "images": images}
    if request.is_ajax():
        return render(request, "images/list_ajax.html", context)

    return render(request, "images/list.html", context) 





    


