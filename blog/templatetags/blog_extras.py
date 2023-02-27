from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(user, currrent_user = None):
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