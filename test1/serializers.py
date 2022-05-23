from rest_framework import serializers
from .models import Post, Comment
# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     desc = serializers.CharField()
#     author = serializers.CharField()
#     create_date = serializers.DateTimeField()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id','title']
        fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['id','author', 'desc']
        fields = '__all__'