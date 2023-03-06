import logging
from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Post, Tag


logger = logging.getLogger(__name__)

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        
        
class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
            slug_field="value", many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=get_user_model().objects.all(), view_name="api_user_detail", lookup_field="email", required=False
    )
    
    class Meta:
        model = Post
        fields = "__all__"
        readonly = [
            "modified_at", 
            "created_at", 
            "author"
        ]
        extra_kwargs = {
            "author": {
                "required": False
            }
        } 
        
    def validate(self, data):
        request = self.context.get('request', None)
        if not request:
            return data
        
        method = request.method
        if method != 'POST':
            return data
        
        user = request.user
        validate_data = data
        validate_data['author'] = data.get('author', user)
        logger.debug("author is %s", validate_data['author'])
            
        return validate_data   
    
