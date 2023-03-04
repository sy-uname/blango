from django.urls import path, include
from blango_auth.views import profile
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

urlpatterns = [
    # other patterns
    path("", include("django.contrib.auth.urls")),
    path("profile/", profile, name="blog-profile"),
    path(
        "register/", 
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
        ),
    path("", include("django_registration.backends.activation.urls")),
]