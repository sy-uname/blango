import logging
from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Post, Tag, Comment


logger = logging.getLogger(__name__)

    
class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            logger.debug("TagField with %s", data)
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")
            
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        
        
class PostSerializer(serializers.ModelSerializer):
    tags = TagField(
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
                "required": False,
            },
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


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]
        
                   
class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        try:
            comments = validated_data.pop("comments")
        except KeyError:
            comments = dict()

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()

        return instance
    
                        