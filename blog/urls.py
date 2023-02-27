from django.urls import path
from blog import views 

urlpatterns = [
    # other patterns
    path("", views.index)
]