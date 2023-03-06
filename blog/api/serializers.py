import logging
from rest_framework import serializers
from blog.models import Post


logger = logging.getLogger(__name__)


class PostSerializer(serializers.ModelSerializer):
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
    