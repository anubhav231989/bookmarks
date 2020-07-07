from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, ProfileForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, FanFollowing
from django.contrib import messages
from actions.utils import register_action
from actions.models import Action
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

def account_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login Success!!")
                else:
                    return HttpResponse("User deactivated!!")
            else:
                return HttpResponse("Invalid Credentials!!")
    else:
        login_form = LoginForm()
        return render(request, "account/login.html", {"login_form": login_form})

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            profile,new = Profile.objects.get_or_create(user=user)
            # REGISTERING ACTION TO BE USED IN ACTIVITY FEED.
            register_action(user, "has joined the platform")
            
            return render(request, "account/register_done.html", {"user": user})
        else:
            return render(request, "account/register.html", {"form": form})
    else:
        form = UserRegistrationForm()
        return render(request, "account/register.html", {"form": form})

@login_required
def edit_user_details(request):
    if request.method == "POST":
        profile_form = ProfileForm(instance=request.user.profile,data=request.POST, files=request.FILES)
        user_form = UserEditForm(instance=request.user,data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Error updating your profile.")
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserEditForm(instance=request.user)

    return render(request, "account/edit_user_details.html", {"user_form": user_form, "profile_form": profile_form})

@login_required
def dashboard(request):
    actions = Action.objects.exclude(user=request.user)
    follower_ids = request.user.profile.following.values_list("id", flat=True)
    if follower_ids:
        actions.filter()
    
    return render(request, "account/dashboard.html", {"section": "dashboard", "actions": actions})

class ProfileList(ListView):
    context_object_name = "profiles"
    template_name = "account/profiles.html"

    # ACCESS REQUEST OBJECT IN THIS METHOD, EXCLUDE SELF PROFILE FROM QUERYSET.
    def get_queryset(self):
         return Profile.objects.select_related("user").filter(user__is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "people"
        return context
class ProfileDetail(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "account/profile_details.html"

# @require_POST
# @ajax_required
@login_required
def start_following(request):
    profile_id = request.POST.get("id",3)
    action = request.POST.get("action","follow")
    if profile_id and action:
        profile = Profile.objects.get(id=profile_id)
        request_user_profile = request.user.profile
        if action == "follow":
            follower,new = FanFollowing.objects.get_or_create(profile_from=request_user_profile, profile_to=profile)
            # REGISTERING ACTION TO BE USED IN ACTIVITY FEED.
            register_action(request.user, "is following", profile.user)
        elif action == "unfollow":
            FanFollowing.objects.filter(profile_from=request_user_profile, profile_to=profile).delete()

        return JsonResponse({"status": "SUCCESS"})

    return JsonResponse({"status": "ERROR"})
        




    
                


