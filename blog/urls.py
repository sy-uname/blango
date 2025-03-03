from django.urls import path
from blog import views 

urlpatterns = [
    # other patterns
    path("", views.index, name="blog-home-page"),
    path("post/<int:pk>", views.post_detail, name="blog-post-detail"),
    path("post-table/", views.post_table, name="blog-post-table"),
    path("ip/", views.get_ip, name="url_get_ip"),
]

