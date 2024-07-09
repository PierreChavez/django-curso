from rest_framework.serializers import ModelSerializer
from posts.models import  Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'date_posted']
        #fields = '__all__'