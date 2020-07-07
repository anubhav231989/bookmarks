Social Website Bookmarks for sharing images.

Django Authentication Framework.

When a new django project is started, django authentication framework(django.contrib.auth) is added to the installed apps by default. Along with two middleware classes(AuthenticationMiddleware, SessionMiddleware).

    Authentication Middleware: handles associating users with requests using sessions.
    Session Middleware: handles the current session across requests.

Django Authentication includes following models as well:
    User.
    Groups.
    Permissions.

It also includes default authentication related views and forms.

Create a login view, which will do following things:
    Get username and password from request and pass it to login form.
    Authenticate the user against the data stored in database.
    Check whether user is active.
    Redirect the user to corresponding screen depending upon the authentication.

Default Django Authentication Views, django.contrib.auth.views
    LoginView, handles login form and logs in a user.
    LogoutView, logouts a user.

Django also provides views to handle password change and reset.
    PasswordChangeView
    PasswordChangeDoneView
    PasswordResetView
    PasswordResetDoneView
    PasswordResetConfirmView
    PasswordCompleteView

registration is the default template directory where django expects the templates to be.
By Default after successful login, django redirects to "accounts/profile/" url. You can override this behaviour using setting LOGIN_REDIRECT in settings.py

By default django authentication login view uses AuthenticationForm(django.contrib.auth.forms) which tries to authenticate the user and raises a validation error if the login was unsuccessful.

LOGIN_URL: where to redirect the user for login.
LOGIN_REDIRECT_URL: where to redirect user after successful login.
LOGOUT_URL: where to redirect the user for logout.

Django has built in one-time notifications to the users. Messages framework. 
django.contrib.messages and a middleware django.contrib.messages.middleware.MessageMiddleware

from django.contrib import messages
message.success(request, "Yo.")

Custom Authentication backend.
Python class with two mandatory functions.
    authenticate(request, username=None, password=none)
    It returns an user object if credentials are valid or None.
    get_user(request, user_id) return user object given user_id.


https://localhost:9000/images/create/?title=bricks&url=https://images.unsplash.com/photo-1591788788843-93d40443bddd?ixlib=rb-1.2.1&auto=format&fit=crop&w=1275&q=80



https://stackoverflow.com/questions/46349459/chrome-neterr-cert-authority-invalid-error-on-self-signing-certificate-at-loca
