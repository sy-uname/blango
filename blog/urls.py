from django.urls import path
from blog import views 

urlpatterns = [
    # other patterns
    path("", views.index),
    path("post/<int:pk>", views.post_detail, name="blog-post-detail"),
]