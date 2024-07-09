from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post

class PostApiView(APIView):
    def get(self, request):
        posts = [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data={'data': posts})

    def post(self, request):
        post = Post.objects.create(title=request.POST['title'], content=request.POST['content'], created_at=request.POST['created_at'])
        return Response(status=status.HTTP_201_CREATED, data={'message': 'Post created', 'data': {'title': post.title, 'id': post.id, 'created_at': post.created_at, 'date_posted': post.date_posted}})