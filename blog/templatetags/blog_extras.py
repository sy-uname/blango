from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from blog.models import Post
import logging


logger = logging.getLogger(__name__)

register = template.Library()
user_model = get_user_model()


@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    user = None
    post = context.get("post", None)
    if post:
        user = post.author
        
    return author_details_api(user, current_user)    


@register.filter
def author_details(user, currrent_user=None):
    return author_details_api(user, currrent_user)        
    
    
def author_details_api(user, currrent_user):
    prefix = ""
    suffix = ""
    if not isinstance(user, user_model):
        result = ""        
    else:
        if user == currrent_user:
            result = format_html("<strong>me</strong>")
        elif user.first_name or user.last_name:
            result = f"{user.first_name} {user.last_name}"
        else:
            result = user.username
        
        if user.email:        
            prefix = format_html('<a href="mailto:{}">', user.email)
            suffix = format_html("</a>")
    
    return mark_safe(f"{prefix}{result}{suffix}")


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return format_html("</div>")


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}

